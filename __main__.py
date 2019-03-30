import random
import string
import time
import setlx
   
from setlx.node import BinaryNode
from setlx.tree import Tree
random = random.Random(27121998)

b = BinaryNode("Schinken", "Bratwurst")
bt = BinaryNode("Bier", "Auflauf")
t = Tree(b)
t2 = Tree(bt)
s = setlx.Set(t)
s2 = setlx.Set(2, 3)
s2[2] = "Yeah it works"
print(setlx.range(s2))