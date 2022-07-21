import sys
from pathlib import Path
from test.cunit import SRC, CModule

CFLAGS = ["-g", "-fprofile-arcs", "-ftest-coverage"]

print("start compile " + __name__)
print(__name__)
print(SRC / Path(__file__).stem)
#sys.modules[__name__] = SRC / Path(__file__).stem
sys.modules[__name__] = CModule.compile(SRC / Path(__file__).stem, cflags=CFLAGS)
print("end compile")
print(sys.modules)
