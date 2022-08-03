from test.cunit import C
from test.cunit.cache import QueueItem

value = C.malloc(16)
queue_item = QueueItem(value, 42)
queue_item.destroy(C.free)