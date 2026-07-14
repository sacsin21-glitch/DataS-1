import sys
print("Python executable:", sys.executable)
print()

print("Python search path:")
for path in sys.path:
    print(path)


import numpy as np
print("NumPy version:", np.__version__)
print("NumPy location:", np.__file__)

print(type(np))