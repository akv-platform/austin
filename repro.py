import ctypes
from test.cunit import C
from test.cunit.cache import QueueItem

C.malloc.restype = ctypes.c_void_p
C.free.argtypes = [ctypes.c_void_p]

value = C.malloc(16)
print("----- value -->", flush=True)
print(hex(value), flush=True)
queue_item = QueueItem(value, 42)
print("----------> ", flush=True)
print(queue_item)
#print(queue_item.key)
#print(queue_item.value)
print("^^^^^^^^^^^^", flush=True)
queue_item.destroy(C.free)
print("==============", flush=True)