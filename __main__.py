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
max_ii = 50
rands = [random.randint(1, max_i) for i in range(0, max_ii)]
s1 = SplaySet()
s2 = SplaySet()
for i in range(0, max_ii):
    s1.insert(List(["speck",rands[max_ii - i - 1]]))
    s2 += SplaySet(rands[i])
print(s1)
print(s2)
print(s1["speck"])
s1["speck"] = "siebzehn"
print(s1["speck"])