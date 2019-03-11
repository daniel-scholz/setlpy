from setlx.native import isList, isMap, isProbablePrime
from setlx.node import BinaryNode
from setlx.tree import Tree
from setlx.set import Set
import random

# trees need to be iterable in order to work

my_set = Set(range(2, 10))
my_set += Set(range(11, 100, 10))
print(my_set)  # {2, 3, 4, 5, 6, 7, 8, 9, 11, 21, 31, 41, 51, 61, 71, 81, 91}
my_set -= Set(range(51, 100, 10))
print(my_set)  # {2, 3, 4, 5, 6, 7, 8, 9, 11, 21, 31, 41}
