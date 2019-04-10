import random
import string
import time

import setlx
from setlx.node import BinaryNode
# from setlx.set import Set
from setlx.splayset import Set 
from setlx.list import List
random = random.Random(0)
max_i = 100
max_ii = 4
rands = [random.randint(1, max_i) for i in range(0, max_ii)]
s1 = Set()
list1 = []
for i in range(1, max_ii):
    newvariable148 = List([i,max_i])
    s1.insert(newvariable148)
    list1+= [i + 1000]

# print(s1.powerset())
print(s1[1])