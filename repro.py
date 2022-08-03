from test.cunit import C
from test.cunit.cache import QueueItem

value = C.malloc(16)
queue_item = QueueItem(value, 42)
print("----------> ")
#print(queue_item)
#print(queue_item.key)
#print(queue_item.value)
print("^^^^^^^^^^^^")
queue_item.destroy(C.free)