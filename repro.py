from ctypes import CDLL

C = CDLL("libc.so.6")
value = C.malloc(16)
C.free(value)