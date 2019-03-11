from setlx.native import isList, isMap, isProbablePrime
from setlx.node import BinaryNode
from setlx.tree import Tree
from setlx.set import Set
import random

numbers = [2, 12, 1]

o = Tree(10)
print(o)
s = Tree(BinaryNode(10))
for n in numbers:
    o.insert(n)
    s.insert(n)
# trees need to be iterable in order to work
print(s > o)

# random.Random(42).shuffle(my_list)
my_set = Set(i for i in range(0, 10))
print(my_set)
