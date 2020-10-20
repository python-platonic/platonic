from platonic.const import const


def test_const():
    """Test the const function."""
    one = const(1)
    bazooka = const('bazooka')

    assert one() == 1
    assert bazooka() == 'bazooka'
