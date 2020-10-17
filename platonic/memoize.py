import functools
from typing import Callable, MutableMapping, TypeVar

KeyType = TypeVar('KeyType')
ValueType = TypeVar('ValueType')


def memoize(
    mapping: MutableMapping[KeyType, ValueType],
):
    """Cache the responses of the given function in the mapping."""
    def _decorator(func: Callable[[KeyType], ValueType]):  # noqa: WPS430
        @functools.wraps(func)
        def wrapper(key: KeyType) -> ValueType:  # noqa: WPS430
            try:
                return mapping[key]

            except KeyError:
                calculated_value = func(key)
                mapping[key] = calculated_value
                return calculated_value

        return wrapper

    return _decorator
