"""
Key-value Mapping.

This module is a draft.
"""

from abc import ABC
from functools import cached_property
from typing import Callable, Mapping, Type, TypeVar

from typecasts import Typecasts

from platonic.type_args import generic_type_args

KeyType = TypeVar('KeyType')
ValueType = TypeVar('ValueType')
InternalType = TypeVar('InternalType')


class PlatonicMapping(
    Mapping[KeyType, ValueType],
    ABC,
):
    """Abstract Mapping definition."""

    internal_type: type
    typecasts: Typecasts

    @cached_property
    def key_type(self) -> Type[KeyType]:
        """Type of the keys."""
        return generic_type_args(self)[0]

    @cached_property
    def value_type(self) -> Type[ValueType]:
        """Type of the values."""
        return generic_type_args(self)[1]

    @cached_property
    def serialize_key(self) -> Callable[[KeyType], InternalType]:
        """Convert key into internal representation."""
        return self.typecasts[self.key_type, self.internal_type]

    @cached_property
    def deserialize_key(self) -> Callable[[InternalType], KeyType]:
        """Restore key from internal representation."""
        return self.typecasts[self.internal_type, self.key_type]

    @cached_property
    def serialize_value(self) -> Callable[[ValueType], InternalType]:
        """Convert value into internal representation."""
        return self.typecasts[self.value_type, self.internal_type]

    @cached_property
    def deserialize_value(self) -> Callable[[InternalType], ValueType]:
        """Restore value from internal representation."""
        return self.typecasts[self.internal_type, self.value_type]
