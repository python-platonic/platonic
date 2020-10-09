import dataclasses
from abc import ABC, abstractmethod
from functools import cached_property
from typing import Generic, Iterable, TypeVar, Type, Callable, NewType

from documented import DocumentedError
from typecasts import Typecasts

from platonic import generic_type_args

ValueType = TypeVar('ValueType')

InternalType = NewType('InternalType', str)
"""We believe most backends work with strings as internal data type."""


class BaseQueue(ABC, Generic[ValueType]):
    """Base class for queues."""

    internal_type: Type[InternalType]
    typecasts: Typecasts

    @cached_property
    def value_type(self) -> Type[ValueType]:
        """Extract the type of queue message from type args."""
        return generic_type_args(self)[0]


@dataclasses.dataclass
class Message(Generic[ValueType]):
    """Queue message."""

    value: ValueType


class InputQueue(Iterable[Message[ValueType]], BaseQueue[ValueType]):
    """Queue to read stuff from."""

    @cached_property
    def deserialize_value(self) -> Callable[[InternalType], ValueType]:
        """Deserialize a queue item from internal representation."""
        return self.typecasts[self.internal_type, self.value_type]

    @abstractmethod
    def receive(self) -> Message[ValueType]:
        """
        Get next message from queue, without deleting it.

        `get` is probably not a good name (see Kevlin Henney), but
        here we are following the example of queue.Queue class from
        the standard library.
        """

    @abstractmethod
    def acknowledge(self, message: Message[ValueType]) -> Message[ValueType]:
        """
        Indicate that the given message is correctly processed.

        By semantics, is equivalent to `queue.Queue.task_done()`.
        """

    @abstractmethod
    def acknowledgement(self, message: Message[ValueType]):
        """
        Into this context manager, you can wrap any operation with a given
        Message. The context manager will automatically acknowledge the message
        when and if the code in its context completes successfully.
        """


class OutputQueue(BaseQueue[ValueType]):
    """Queue to write stuff into."""

    @cached_property
    def serialize_value(self) -> Callable[[ValueType], InternalType]:
        """Serialize a queue item into internal representation."""
        return self.typecasts[self.value_type, self.internal_type]

    @abstractmethod
    def send(self, instance: ValueType) -> Message[ValueType]:
        """
        Push a message into the queue.

        See `InputQueue.get()` about naming controversy.
        """

    def send_many(self, iterable: Iterable[ValueType]) -> None:
        """Put multiple messages into the queue."""
        for instance in iterable:
            self.send(instance)


@dataclasses.dataclass
class QueueDoesNotExist(DocumentedError, Generic[ValueType]):
    """Specified queue does not exist."""

    queue: BaseQueue[ValueType]


@dataclasses.dataclass
class MessageDoesNotExist(DocumentedError, Generic[ValueType]):
    """Specified message {self.message} does not exist in the queue."""

    message: Message[ValueType]
    queue: InputQueue[ValueType]


@dataclasses.dataclass
class MessageTooLarge(DocumentedError):
    """
    Message is too large.

    Provided message size is {self.message_size} bytes, while
    maximum message size is {self.max_supported_size} bytes.

    Message preview:
        {self.message_head}...{self.message_tail}
    """

    max_supported_size: int
    message_body: str

    message_preview_size: int = 10

    @property
    def message_head(self):
        """First N bytes of the message."""
        return self.message_body[:self.message_preview_size]

    @property
    def message_tail(self):
        """Last N bytes of the message."""
        return self.message_body[-self.message_preview_size:]

    @property
    def message_size(self) -> int:
        return len(self.message_body)
