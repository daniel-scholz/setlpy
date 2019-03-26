from setlx.node import BinaryNode
from setlx.tree import Tree

import copy
from types import GeneratorType
import itertools


class Set():
    # https://stackoverflow.com/questions/19151/build-a-basic-python-iterator
    def __init__(self, arg=None):
        if isinstance(arg, Tree):  # not sure if this is necessary
            self.tree = arg
        elif not isinstance(arg, (GeneratorType, range)) or arg == None:
            self.tree = Tree(arg)
        else:
            try:
                """
                check if argument for constructor is an iterable like list, set etc.
                """
                self.tree = Tree()
                for element in iter(arg):
                    self.tree.insert(element)
            except TypeError:
                raise TypeError(
                    f"set cannot be created from {type(arg)}")

    def __iter__(self):
        new_set = Set(self.tree)
        new_set.tree.index = 0
        # minimum of the tree
        # self.tree.current_node = self.tree[0] if self.tree.total > 0 else None
        return new_set

    def __next__(self):
        return next(self.tree).key

    def __arb__(self):
        if self.tree.total < 1:
            return None
        if self.tree.total % 2 == 0:
            return self.tree[0].key
        else:
            return self.tree[-1].key


    def __getitem__(self, index):
        if isinstance(index, slice):
            start = index.start if index.start != None else 0
            stop = index.stop if index.step != None else self.tree.total
            step = index.step if index.step != None else 1
            return Set(self[i] for i in range(start, stop, step))
        item = self.tree[index]
        return item.key if isinstance(item, BinaryNode) else item

    def __len__(self):
        return self.tree.total

    def __from__(self):
        # look up SetlX implementation
        return self.tree[0]

    def first(self):
        return self.tree[0]

    def last(self):
        return self.tree[-1]

    def __str__(self):
        return "{" + ", ".join("'" + self[i].key + "'" if type(self[i].key) == str else str(self[i]) for i in range(0, self.tree.total))+"}"

    def __repr__(self):
        return self.__str__()

    """https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types"""

    def __add__(self, other):
        # add elements/ union of two sets
        new_set = Set(self.tree)
        # for s in self:
        # new_set.insert(s)

        if not isinstance(other, (Set, Tree)):
            new_set.insert(other)
        elif len(other) != 0:  # is not empty set
            for o in other:
                new_set.insert(o)
        return new_set

    def __sub__(self, other):
        # remove from self
        new_set = Set(self.tree)

        if not isinstance(other, (Set, Tree)):
            new_set.tree.delete(other)
        else:
            for o in other:
                if o in self:
                    try:
                        new_set.tree.delete(o)
                    except (ValueError):
                        raise TypeError(
                            f"could not delete {o} from set")
        return new_set

    def __mul__(self, other):
        # intersection
        if not isinstance(other, Set):
            raise TypeError(f"could not intersect set and {type(other)}")
        else:
            others = iter(other)  # raises TypeError if not castable
            return Set(x for x in others if x in self)

    # matrix multiplication; "@" operator
    # def __matmul__(self, other):
        # pass

    def __mod__(self, other):
        # “%” computes the symmetric difference of two sets.
        self_copy = self[:]
        s1 = (self - other)
        s2 = (other - self_copy)
        return s1 + s2

    def __pow__(self, other, modulo=None):
        # ** operator
        if other == 2:
            new_set = Set()
            for s1 in self:
                for s2 in self:
                    new_set += (s1, s2)
            return new_set
        raise TypeError(f"{other} must be 2 to computer cartesian product")

    def __and__(self, other):
        pass

    def __xor__(self, other):
        # ^
        return self % other

    def __le__(self, other):  # a.k.a. is_subset
        """
        corresponds to self <= other
        implements check for subset, NOT real less or equal
        other is subset of self; all elements of self are in other
        """
        if other != None and self != None:  # and other.tree != None and self.tree != None:
            return self.tree <= other.tree
        return False

    def __lt__(self, other):
        """
        implements check for real subset, NOT real less
        """
        return self.tree != other.tree and self.tree <= other.tree

    def __gt__(self, other):
        """
        returns self > other
        """
        return other < self

    def __ge__(self, other):
        """
        returns self >= other
        """
        return other <= self
    # extracts key from nnode

    def find(self, key):
        return self.tree.find(key)

    def insert(self, key):
        self.tree.insert(key)


def arb(s):
    try:
        return s.__arb__()
    except:
        raise Exception(f"arb not defined on type {type(s)}")


def pow(x, y):
    if type(y) == Set:
        if x == 2:
            if len(y) == 0:
                return Set(Set())
            element = y[0]

            return pow(2, y[1:]) + Set(element) + pow(2, y[1:])

        raise ValueError(f"{x} must be 2 to compute power set")
    return x ** y
