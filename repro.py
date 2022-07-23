from ctypes import cdll, sizeof, cast
from ctypes.util import find_library
import ctypes

def load_libc():
    """
    Loads C standard library and setup argtypes and restype.
    We wrap this in a function to we have a central point of access to these
    functions.
    """

    libc = cdll.LoadLibrary(find_library("c"))

    # To be safe we setup argtypes, and restypes for functions we pass arguments
    # to and also the return type for functions we use the return value
    #
    # NOTE: printf is variable arg, so one should setup argtypes before each
    #       call for non-variable arg, one only has to setup types once.

    # Call 'malloc' we setup argument type and return type
    libc.malloc.argtypes = [ctypes.c_size_t]
    libc.malloc.restype = ctypes.c_void_p
    libc.free.argtypes = [ctypes.c_void_p]

libc = load_libc()
nelem = 100
libc.printf.argtypes = [ctypes.c_char_p]
libc.printf("Hello World via Python -> libc\n")

#C = CDLL("libc.so.6")
#print("55555555555")
#value = C.malloc(16)
#print("==========")
#v1=value
#print("v1")
#print(v1)
#print("value=>")
#print(value)
#C.free(value)