from test.cunit import C
from test.cunit.cache import QueueItem


NULL = 0


def test_queue_item():
    value = C.malloc(16)
    print("test_queue_item")
    print(value)
    print("test_queue_item new QueueItem")
    queue_item = QueueItem(value, 42)
    assert queue_item.__cself__

    print("test_queue_item queue_item destroy")
    queue_item.destroy(C.free)