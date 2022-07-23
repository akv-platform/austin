from ctypes import CDLL

C = CDLL("libc.so.6")

value = C.malloc(16)
print("==========")
v1=value
print("v1")
print(v1)
print("value")
print(value)
C.free(value)
