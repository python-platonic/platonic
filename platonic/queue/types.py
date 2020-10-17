from typing import TypeVar, NewType


ValueType = TypeVar('ValueType')

InternalType = NewType('InternalType', str)
"""We believe most backends work with strings as internal data type."""
