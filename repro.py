import ctypes
from test.cunit import C
from test.cunit.cache import QueueItem
import test.cunit.cache 

print(dir(test.cunit.cache))
print(dir(test.cunit.cache.QueueItem))


#print("free __annotations__", flush=True)
#print(C.free.__annotations__, flush=True)

#print("QueueItem.new __annotations__", flush=True)
#print(test.cunit.cache.QueueItem.new.__annotations__)
#print("QueueItem.new.argtypes", flush=True)
#print(test.cunit.cache.QueueItem.new.argtypes, flush=True)

C.malloc.restype = ctypes.c_void_p
C.free.argtypes = [ctypes.c_void_p]

# just make sure malloc/free works
p = C.malloc(16)
C.free(p)
print("malloc/free works", flush=True)

cache = ctypes.CDLL("src/cache.so")
print(cache)
exit(0)


print(test.cunit.cache.QueueItem.new, flush=True)
print(test.cunit.cache.QueueItem.__new__, flush=True)

test.cunit.cache.QueueItem.new.argtypes = [ctypes.c_void_p, ctypes.c_long]
test.cunit.cache.QueueItem.__new__.argtypes = [ctypes.c_void_p, ctypes.c_long]

value = C.malloc(16)
print("----- value -->", flush=True)
print(hex(value), flush=True)
queue_item = test.cunit.cache.QueueItem.new(value, 42)
queue_item = QueueItem(value, 42)
print("----------> ", flush=True)
print(hex(id(queue_item)), flush=True)
print(ctypes.byref(queue_item), flush=True)
#print(hex(ctypes.byref(queue_item)), flush=True)
#print(queue_item.key)
#print(queue_item.value)
print("^^^^^^^^^^^^", flush=True)
queue_item.destroy(C.free)
print("==============", flush=True)