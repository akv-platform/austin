from test.cunit import C
from test.cunit.cache import QueueItem
import ctypes

NULL = 0

C.malloc.restype = ctypes.c_void_p
C.free.argtypes = [ctypes.c_void_p]

def test_queue_item():

    value = C.malloc(16)
    queue_item = QueueItem(value, 42)
    assert queue_item.__cself__
    queue_item.destroy(C.free)
