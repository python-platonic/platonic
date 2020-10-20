from typing import Generic, TypeVar

import pytest

from platonic.type_args import TypeArgsError, generic_type_args

Type1 = TypeVar('Type1')
Type2 = TypeVar('Type2')


@pytest.mark.parametrize(('generic_type', 'type_parameters'), [
    (Generic[Type1], (Type1, )),
    (Generic[Type1, Type2], (Type1, Type2)),
])
def test_generic(generic_type, type_parameters):
    """Tests for typing.Generic."""
    assert generic_type_args(generic_type) == type_parameters


def test_dict():
    """Test just a simple dict."""
    with pytest.raises(TypeArgsError):
        generic_type_args({})
