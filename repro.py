import ctypes
from test.cunit import C
from test.cunit.cache import QueueItem
import test.cunit.cache 

print(dir(test.cunit.cache))

C.malloc.restype = ctypes.c_void_p
C.free.argtypes = [ctypes.c_void_p]

value = C.malloc(16)
print("----- value -->", flush=True)
print(hex(value), flush=True)
queue_item = QueueItem(value, 42)
print("----------> ", flush=True)
print(hex(id(queue_item)), flush=True)
#print(queue_item.key)
#print(queue_item.value)
print("^^^^^^^^^^^^", flush=True)
queue_item.destroy(C.free)
print("==============", flush=True)