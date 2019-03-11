from setlx.native import isList, isMap, isProbablePrime
from setlx.node import BinaryNode
from setlx.tree import Tree
from setlx.set import Set
import random

# trees need to be iterable in order to work

my_set = Set(range(1, 4))
print(my_set)
my_set2 = Set(range(3, 6))
print(my_set2)

print(my_set % my_set2)
