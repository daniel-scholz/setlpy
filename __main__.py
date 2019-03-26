import random
import string

import setlx
random = random.Random(27121998)

s1 = setlx.Set(range(0, 5))
s2 = s1[:]
s1 = s1 - 3
print(s1 - 3)
print(s2)
