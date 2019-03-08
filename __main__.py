from setlx.native import isList, isMap, isProbablePrime
from setlx.node import BinaryNode
from setlx.tree import Tree
from setlx.set import Set


o = Tree(BinaryNode(10))
o.insert(BinaryNode(2))
o.insert(BinaryNode(12))
o.insert(BinaryNode(1))

s = Tree(BinaryNode(10))
s.insert(BinaryNode(2))
s.insert(BinaryNode(12))
s.insert(BinaryNode(1))

# print("other:", o)
# print("self:", s)
# trees need to be iterable in order to work
# print(s > o)

for node in s:
    print(node)
my_set = Set(s)

for node in my_set:
     print(node)

print(max(my_set))