import random
import string
import time

from setlx.node import BinaryNode
from setlx.tree import Tree
from setlx.splayset import Set as SplaySet
from setlx.set import Set
random = random.Random(27121998)
max_i = 100
max_ii = 10
rands = [random.randint(1, max_i) for i in range(0, max_ii)]

s1 = SplaySet()
s2 = SplaySet()
for i in range(0, max_ii):
    s1 += rands[max_ii - i - 1]
    s2 += rands[i]

for s in s1:
    for ss in s2:
        print(f"{s}:{ss:}")

print(s1, s2, sep="\n")
print(s1 ** 2)
