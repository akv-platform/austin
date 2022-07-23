from ctypes import CDLL
import ctypes

C = CDLL("libc.so.6")
C.malloc.restype = ctypes.c_void_p
C.free.argtypes = [ctypes.c_void_p]

value = C.malloc(16)
C.free(value)