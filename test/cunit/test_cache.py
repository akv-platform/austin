from test.cunit import C
from test.cunit.cache import QueueItem


NULL = 0


def test_queue_item():
    value = C.malloc(32)
    C.free(value)