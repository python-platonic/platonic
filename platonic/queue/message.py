import dataclasses
from typing import Generic

from platonic.queue.types import ValueType


@dataclasses.dataclass
class Message(Generic[ValueType]):
    """Queue message."""

    value: ValueType  # noqa: WPS110
