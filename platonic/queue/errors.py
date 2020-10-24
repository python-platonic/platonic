import dataclasses

from documented import DocumentedError

from platonic.queue.base import BaseQueue
from platonic.queue.input import InputQueue, Message


@dataclasses.dataclass
class MessageReceiveTimeout(DocumentedError):
    """
    No messages received within {self.timeout} {self.readable_time_suffix}.

      Queue: {self.queue}
    """

    queue: InputQueue
    timeout: int

    @property
    def readable_time_suffix(self) -> str:
        """Second or seconds."""
        if self.timeout == 1:
            return 'second'

        return 'seconds'


@dataclasses.dataclass
class QueueDoesNotExist(DocumentedError):
    """Specified queue does not exist."""

    queue: BaseQueue


@dataclasses.dataclass
class MessageDoesNotExist(DocumentedError):
    """Specified message {self.message} does not exist in the queue."""

    message: Message
    queue: InputQueue


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
