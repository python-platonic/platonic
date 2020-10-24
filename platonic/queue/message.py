import dataclasses
from typing import Generic, TypeVar

MessageValueType = TypeVar('MessageValueType')


@dataclasses.dataclass
class Message(Generic[MessageValueType]):
    """Queue message."""

    value: MessageValueType  # noqa: WPS110
