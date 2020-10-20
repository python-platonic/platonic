from dataclasses import dataclass
from typing import Any, Iterator, Tuple, get_args

from documented import DocumentedError


@dataclass
class TypeArgsError(DocumentedError):   # type: ignore
    """
    Cannot ascertain type arguments from intance or class.

    Object: {self.instance}
    """

    instance: Any   # type: ignore


def iterate_by_type_parameters(  # type: ignore
    instance: Any,
) -> Iterator[Tuple[type, ...]]:
    """Iterate over classes in MRO and yield type parameters for each."""
    try:
        yield get_args(instance.__orig_class__)   # noqa: WPS609
    except AttributeError:
        pass

    try:
        yield from map(
            get_args,
            instance.__orig_bases__,  # noqa: WPS609
        )
    except AttributeError:
        pass

    if instance_args := get_args(instance):
        yield instance_args


def generic_type_args(instance: Any) -> Tuple[type, ...]:  # type: ignore
    """Get type parameters given a class instance."""
    try:
        type_parameters, *etc = iterate_by_type_parameters(instance)
    except ValueError:
        raise TypeArgsError(instance=instance)

    return type_parameters
