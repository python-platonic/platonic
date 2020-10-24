from abc import abstractmethod
from functools import cached_property
from typing import Callable, Iterable

from platonic.queue.base import BaseQueue
from platonic.queue.message import Message
from platonic.queue.types import InternalType, ValueType


class InputQueue(Iterable[Message[ValueType]], BaseQueue[ValueType]):
    """Queue to read stuff from."""

    @cached_property
    def deserialize_value(self) -> Callable[[InternalType], ValueType]:
        """Deserialize a queue item from internal representation."""
        return self.typecasts[  # pragma: no cover
            self.internal_type,
            self.value_type,
        ]

    @abstractmethod
    def receive(self) -> Message[ValueType]:
        """Get next message from queue, without deleting it."""

    @abstractmethod
    def receive_with_timeout(self, timeout: int) -> Message[ValueType]:
        """
        For the given period of time, wait for a new message from the queue.

        Return the message if received, otherwise throw a ReceiveTimeout error.
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
        Acknowledgement context manager.

        Into this context manager, you can wrap any operation with a given
        Message. The context manager will automatically acknowledge the message
        when and if the code in its context completes successfully.
        """
