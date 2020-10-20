from platonic.queue.base import BaseQueue


class ConcreteBaseQueue(BaseQueue[int]):
    """Queue of ints."""


def test_base_queue_value_type():
    """Test value type."""
    assert ConcreteBaseQueue().value_type == int
