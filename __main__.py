import random
import string
import time

import setlx
from setlx.node import BinaryNode
from setlx.splayset import Set 
from setlx.list import List
random = random.Random(0)
max_i = 5
max_ii = 5
rands = [random.randint(1, max_i) for i in range(0, max_ii)]
s1 = Set()
for i in range(1, max_ii):
    newvariable148 = rands[i]
    s1.insert(newvariable148)

# print(s1.powerset())
print("s1",s1)
s2 = Set([])
print("s2",s2)
print(s1 < s2)
