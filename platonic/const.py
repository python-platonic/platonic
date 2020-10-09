from typing import Callable, TypeVar

ValueType = TypeVar('ValueType')


def const(anything: ValueType) -> Callable[[], ValueType]:
    """Generate a function which always returns the same value."""
    return lambda: anything
