__author__ = 'Su Lei'

import numpy as np

a = np.array([0, 245, 6745, 23112, 2 ** 16 -1], dtype=np.uint16)
print a + 10
b = np.zeros((1, 3), dtype=np.uint8)
b = np.uint8(a)
print b
print (a / (2.0 ** 16 - 1)) * (2 ** 8 - 1)
c = np.uint8((a / (2.0 ** 16 - 1)) * (2 ** 8 - 1))
print c

