from setlx.set import Set
from setlx.node import Node

n = Node(2)
n.left = Node(1)
print(n)

s1 = Set()
s2 = Set()
j = 10
n = 1000

for i in range(1, n):
    s1.insert(i)
    s2.insert(i + 1)

print(s1, s2, sep="\n")
print(s1 <= s2)
