from typing import NewType, TypeVar

ValueType = TypeVar('ValueType')

# We believe most backends work with strings as internal data type.
InternalType = NewType('InternalType', str)
