from setlx.native import isList, isMap, isProbablePrime
from setlx.node import BinaryNode
from setlx.tree import Tree
from setlx.set import Set
import random
import string

random = random.Random(27121998)


class my_random():
    def __init__(self):
        self.i = random.randint(0, 10000)


my_set = Set()
my_set2 = Set()
print(my_set < my_set2)
for i in range(1, 10):
    newvariable638 = {i * 3, i // 2}
    print(newvariable638)
    my_set += newvariable638
    my_set2 += (i//3, i)

print(my_set)
print(my_set2)

letters = string.ascii_letters + string.punctuation + string.digits
my_set = Set()
my_set2 = Set()
for i in range(0, 10):
    rnd_str = "".join(random.choice(letters)
                      for x in range(random.randint(5, 10)))
    my_set += rnd_str
    rnd_str = "".join(random.choice(letters)
                      for x in range(random.randint(5, 10)))
    my_set2 += rnd_str

print(my_set)
print(my_set2)
