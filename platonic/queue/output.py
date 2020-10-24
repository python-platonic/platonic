from abc import abstractmethod
from functools import cached_property
from typing import Callable, Iterable

from platonic.queue.base import BaseQueue
from platonic.queue.message import Message
from platonic.queue.types import InternalType, ValueType


class OutputQueue(BaseQueue[ValueType]):
    """Queue to write stuff into."""

    @cached_property
    def serialize_value(self) -> Callable[[ValueType], InternalType]:
        """Serialize a queue item into internal representation."""
        return self.typecasts[  # pragma: no cover
            self.value_type,
            self.internal_type,
        ]

    @abstractmethod
    def send(self, instance: ValueType) -> Message[ValueType]:
        """
        Push a message into the queue.

        See `InputQueue.get()` about naming controversy.
        """

    def send_many(self, iterable: Iterable[ValueType]) -> None:
        """Put multiple messages into the queue."""
        for instance in iterable:  # pragma: no cover
            self.send(instance)
