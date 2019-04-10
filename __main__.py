import random
import string
import time

import setlx
from setlx.node import BinaryNode
# from setlx.set import Set
from setlx.splayset import Set as SplaySet
from setlx.list import List
random = random.Random(0)
max_i = 100
max_ii = 10
rands = [random.randint(1, max_i) for i in range(0, max_ii)]
s1 = SplaySet(range(1, max_ii))
s1.find(1)
s1.find(2)
for a in s1:
    for b in s1:
        print(a, b)
print(s1**2)