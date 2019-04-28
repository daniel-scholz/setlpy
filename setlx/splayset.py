import copy
import random
from types import GeneratorType

from setlx.list import List
from setlx.splaytree import SplayTree
from setlx.tree import Tree


class Set:
    # https://stackoverflow.com/questions/19151/build-a-basic-python-iterator
    def __init__(self, arg=None):
        if isinstance(arg, Tree):  # [] used for cloning the set
            self.tree = arg
        elif arg is None or not isinstance(arg, (set, GeneratorType, tuple, list, range)):
            self.tree = SplayTree(arg)

        # map feature is implemented in tree class

        # elif isinstance(arg, List) and len(arg) == 2:
        #  self.tree = Tree(key=arg[1], value=arg[2])
        else:
            """
            check if argument for constructor is an iterable like list, set etc.
            """
            self.tree = SplayTree()
            for element in iter(arg):
                self.tree.insert(element)

    def __iter__(self):
        new_set = self._clone()
        new_set.tree.current = self.first()
        # minimum of the tree
        # self.tree.current_node = self.tree[0] if self.tree.total > 0 else None
        return new_set

    def __next__(self):
        nxt = next(self.tree)
        if nxt != None:
            return nxt.key

    def __arb__(self):
        if self.tree.total < 1:
            return None
        if self.tree.total % 2 == 0:
            return self.first()
        else:
            return self.last()

    def __getitem__(self, index):
        result = self.tree[index]
        if result != None:
            return copy.deepcopy(result.key[2])

    def __setitem__(self, key, value):

        self.tree[key] = value

    def _clone(self):
        return Set(self.tree._clone())

    def __len__(self):
        return self.tree.total

    def __from__(self):  # from
        result = self.__arb__()
        self.delete(result)
        return result

    def __fromB__(self):
        result = self.first()
        self -= result
        return result

    def __fromE__(self):
        result = self.last()
        self -= result
        return result

    def first(self):
        if self.tree.root == None:
            return None
        return self.tree.root.min().key

    def last(self):
        if self.tree.root == None:
            return None
        return self.tree.root.max().key

    def __str__(self):
        return "{" + ", ".join(("'" + str(i) + "'") if type(i) == str else str(i) for i in self) + "}"

    def __repr__(self):
        return str(self)

    """https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types"""

    def __add__(self, other):
        # add elements/ union of two sets
        if not isinstance(other, (list, Set)):
            raise TypeError("sets can only be joined with sets")
        new_set = self._clone()
        for element in other:
            new_set.insert(element)
        return new_set

    def __sub__(self, other):
        # remove from self
        new_set = self._clone()  # TODO: deepcopy?
        if not isinstance(other, (Set, Tree)):
            new_set.tree.delete(other)
        else:
            for o in other:
                if o in self:
                    try:
                        new_set.delete(o)
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
        s1 = (self - other)
        s2 = (other - self)
        return s1 + s2

    def __pow__(self, other, modulo=None):
        # ** operator
        if other == 2:
            # cartesian product
            new_set = Set()
            for s1 in self:
                for s2 in self:
                    new_set += Set(List([[s1, s2]]))
            return new_set
        raise TypeError(
            f"{other} must be 2 to compute cartesian product of a set with itself")

    def powerset(self):
        if self._is_empty():
            return Set(Set())

        copy_set = self._clone()
        element = copy_set.__from__()
        power_set = copy_set.powerset()
        result = Set()
        for item in power_set:
            result += Set(Set(element) + item) + Set(item)
        return result

    def __and__(self, other):
        pass

    def __xor__(self, other):
        # ^
        return self % other

    def __eq__(self, other):
        try:
            _ = other.tree
        except AttributeError:
            return False
        return self.tree == other.tree

    def __le__(self, other):  # a.k.a. is_subset
        # and other.tree != None and self.tree != None:
        if other != None and self != None:
            return self.tree <= other.tree
        return False

    def __lt__(self, other):
        if self.tree == None:
            return True
        if other == None or other.tree == None:
            return False
        if self.tree != None and other.tree != None:
            return self.tree < other.tree
        return False

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

    def delete(self, key):
        self.tree.delete(key)

    def insert(self, key):
        self.tree.insert(key)

    def clear(self):
        self.tree = SplayTree()

    def __rnd__(self):
        return self.__arb__()

    def __domain__(self):
        if not self.tree.is_map:
            raise Exception(f"{self} is not a map")

        return Set(k[1] for k in self)

    def __range__(self):
        if not self.tree.is_map:
            raise Exception(f"{self} is not a map")

        new_set = Set()
        for s in self:
            new_set += s[2]
        return new_set

    def _is_empty(self):
        return self.tree.total == 0

    def __hash__(self):
        size = self.tree.total
        _hash = size
        if size >= 1:
            _hash = size * 31 + hash(self.first())
            if size >= 2:
                _hash = _hash*31 + hash(self.last())
        return _hash
