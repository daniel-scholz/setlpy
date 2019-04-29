from setlx.set import Set
from setlx.list import List
from setlx.node import Node
import random

n = Node(2)
n.left = Node(1)
print(n)

s1 = Set()
j = 10
n = 100

for i in range(1, n):
    s1.insert(List([i, random.randint(1, i)]))

print(s1)
print(s1[3])
s2 = Set(s1)
s1[3] = 100
print(s1 + s2)
for s in s1:
    print(s)
print(s1)
print(s2)
print(s1**2)
