from abc import ABC
from functools import cached_property
from typing import Generic, Type, TypeVar

from typecasts import Typecasts

from platonic.queue.types import InternalType
from platonic.type_args import generic_type_args

ValueType = TypeVar('ValueType')


class BaseQueue(ABC, Generic[ValueType]):
    """Base class for queues."""

    internal_type: Type[InternalType]
    typecasts: Typecasts

    @cached_property
    def value_type(self) -> Type[ValueType]:
        """Extract the type of queue message from type args."""
        return generic_type_args(self)[0]
