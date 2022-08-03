from test.cunit import C
from test.cunit.cache import QueueItem


NULL = 0


def test_queue_item():
    value = C.malloc(16)
    queue_item = QueueItem(value, 42)
    assert queue_item.__cself__
    queue_item.destroy(C.free)
