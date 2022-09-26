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

print(C.malloc)
C.malloc.restype = ctypes.c_void_p
C.free.argtypes = [ctypes.c_void_p]

# just make sure malloc/free works
p = C.malloc(16)
C.free(p)
print("malloc/free works", flush=True)

#cache = ctypes.CDLL("src/cache.so")
#print(cache)
#value = C.malloc(16)
#print("----- value pointer-->", flush=True)
#print(hex(value), flush=True)
#print("----- call queue_item_new without argtypes-->", flush=True)
#ret = cache.queue_item_new(value, 42)
#print("----- call queue_item_new without argtypes returned -->", flush=True)
#print(hex(ret))


#cache.queue_item_new.argtypes = [ctypes.c_void_p, ctypes.c_long]
#cache.queue_item_new.restype = ctypes.c_void_p

#print("----- call queue_item_new with argtypes-->", flush=True)
#queue_item = cache.queue_item_new(value, 42)
#print("----- call queue_item_new with argtypes returned -->", flush=True)
#print(hex(queue_item))
#print("----- call queue_item__destroy-->", flush=True)
#cache.queue_item__destroy.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
#cache.queue_item__destroy(0,queue_item)


print(test.cunit.cache.QueueItem.new)
print(test.cunit.cache.QueueItem.new.__cfunc__)
print(test.cunit.cache.QueueItem.new.__cfunc__.argtypes)
test.cunit.cache.QueueItem.new.__cfunc__.argtypes = [ctypes.c_void_p, ctypes.c_long]
test.cunit.cache.QueueItem.new.__cfunc__.restype = ctypes.c_void_p
#test.cunit.cache.QueueItem.destroy.__cfunc__.argtypes = [ctypes.c_void_p, ctypes.c_void_p]

value = C.malloc(16)
print("----- value pointer for test.cunit.cache.QueueItem.new -->", flush=True)
print(hex(value), flush=True)
print("----- call test.cunit.cache.QueueItem.new -->", flush=True)
queue_item = test.cunit.cache.QueueItem.new(value, 42)
print("----- call test.cunit.cache.QueueItem.new returned -->", flush=True)
print(hex(queue_item))

value = C.malloc(16)
print("----- value pointer for QueueItem() -->", flush=True)
print(hex(value), flush=True)
print("----- call QueueItem() -->", flush=True)
queue_item = QueueItem(value, 42)
#print("----------> ", flush=True)
#print(hex(id(queue_item)), flush=True)
print(ctypes.byref(queue_item), flush=True)
#print(hex(ctypes.byref(queue_item)), flush=True)
#print(queue_item.key)
#print(queue_item.value)
print("^^^^^^^^^^^^", flush=True)
queue_item.destroy(C.free)
print("==============", flush=True)