from typing import Any, Iterator, Tuple, get_args


def iterate_by_type_parameters(  # type: ignore
    instance: Any,
) -> Iterator[Tuple[type, ...]]:
    """Iterate over classes in MRO and yield type parameters for each."""
    try:
        classes = (
            instance.__orig_class__,   # noqa: WPS609
            *instance.__orig_bases__,  # noqa: WPS609
        )

    except AttributeError:
        classes = instance.__orig_bases__  # noqa: WPS609

    yield from map(
        get_args,
        classes,
    )


def generic_type_args(instance: Any) -> Tuple[type, ...]:  # type: ignore
    """Get type parameters given a class instance."""
    type_parameters, *etc = iterate_by_type_parameters(instance)
    return type_parameters
