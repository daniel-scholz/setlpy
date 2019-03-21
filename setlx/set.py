from setlx.node import BinaryNode
from setlx.tree import Tree

import copy
from types import GeneratorType


class Set():
    # https://stackoverflow.com/questions/19151/build-a-basic-python-iterator
    def __init__(self, arg=None):
        if isinstance(arg, Tree):  # not sure if this is necessary
            self.tree = arg
        elif not isinstance(arg, (GeneratorType)) or arg == None:
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
        self.tree.index = 0
        self.tree.current_node = self.tree[0]  # minimum of the tree
        return self

    def __next__(self):
        return self.tree.__next__().key

    def __arb__(self):
        return NotImplemented

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
        return "{" + ", ".join(str(self[i]) for i in range(0, self.tree.total))+"}"

    """https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types"""

    def __add__(self, other):
        # add elements/ union of two sets
        # if isinstance(other, Set):
        #     for node in other:
        #         self.tree.insert(node)
        # el
        if not isinstance(other, (Set, Tree)):
            self.tree.insert(other)
        else:
            for o in other:
                try:
                    self.tree.insert(o)
                except TypeError:
                    raise TypeError(
                        f"items of type {type(o)} cannot be add to set of type {type(min(self))}")
        return self

    def __sub__(self, other):
        # remove from self
        if not isinstance(other, (Set, Tree)):
            self.tree.delete(other)
        else:
            for o in other:
                if o in self:
                    try:
                        self.tree.delete(o)
                    except (ValueError):
                        raise TypeError(
                            f"could not delete {o} from set")
        return self

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
        pass

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
        if other != None and self != None:
            return self.tree <= other.tree
        return False

    def __lt__(self, other):
        """
        implements check for real subset, NOT real less
        """
        return self != other and self <= other

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


def arb(s):
    try:
        return s.__arb__()
    except:
        raise Exception(f"arb not defined on type {type(s)}")
