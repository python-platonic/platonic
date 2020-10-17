import dataclasses
from typing import Generic

from documented import DocumentedError

from platonic.queue.base import BaseQueue
from platonic.queue.input import InputQueue, Message
from platonic.queue.types import ValueType


@dataclasses.dataclass
class MessageReceiveTimeout(DocumentedError, Generic[ValueType]):
    """
    No messages received within {self.timeout} {self.readable_time_suffix}.

      Queue: {self.queue}
    """

    queue: InputQueue[ValueType]
    timeout: int

    @property
    def readable_time_suffix(self) -> str:
        """Second or seconds."""
        if self.timeout == 1:
            return 'second'

        return 'seconds'


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
        """Size of the raw message representation, in bytes."""
        return len(self.message_body)
