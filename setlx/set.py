import copy
import random
from types import GeneratorType

from setlx.list import List
from setlx.tree import Tree
from setlx.node import NotAMapError


class Set:
    """ A class which implements sets as they are in SetlX.

    This class serves as wrapper class for the splay tree which is the abstract data structure containing all
    elements of a set.

    """

    def __init__(self, arg=None):
        """__init__ initialises the set with the element(s) in the parameter arg.

        :param arg: A single item or a list of items which will be inserted into the set.
        """
        if arg is None or not isinstance(arg, (set, GeneratorType, tuple, list, range)):
            """
                If the argument only contains a single element, the tree is initialized with it.
                This is also possible for an empty set, when the arg is equal to None. This is the default parameter.
            """
            self.tree = Tree(arg)

        else:
            """
            When argument for constructor is an iterable like list, set etc. each element is inserted separately into
            an empty tree.
            """
            self.tree = Tree()
            for element in arg:
                self.tree.insert(element)

    def __iter__(self):
        """
        This is necessary for the set to be iterable. Initializes a generator object which returns a new node every time
        the set is iterated over.
        :return: Returns a copy of the set to enable nested loops over the same set.
        """
        new_set = self._clone()
        new_set.tree.iterator = self.tree.traverse()
        return new_set

    def __next__(self):
        """Invokes _next__ of the tree attribute.
        :return: The key of the next node in the tree.
        """

        nxt = next(self.tree)
        if nxt is not None:
            return nxt.key

    def __arb__(self):
        """Native Setlx function, which needs to be implemented in Python.

        :return: Returns the first element, when the length of the set is equal, else it returns the last element.
        """
        if self.tree.total < 1:
            return None
        if self.tree.total % 2 == 0:
            return self.first()
        else:
            return self.last()

    def __getitem__(self, key):
        """When the set is used as a map this returns the value of for a certain key. The method call is passed down to
        tree object.

        :param key: Key, for which the value should be returned
        :return: the value, corresponding to the key parameter
        """
        result = self.tree[key]
        if result is not None:
            """This needs to be deep-copied in order not to change the elements in the map via the reference, but
            return the value as in SetlX.
            The index 2 from key implies stands for the value as key-value-pairs are represented as lists of length 2"""
            return copy.deepcopy(result.key[2])

    def __setitem__(self, key, value):
        """Sets value for a specific key in the set."""
        self.tree[key] = value

    def _clone(self):
        """:returns a copy of the current set."""
        new_set = Set()
        new_set.tree = self.tree._clone()
        return new_set

    def __len__(self):
        """:returns the amount of elements in the set"""
        return self.tree.total

    def __from__(self):
        """:returns an arbitrary element and deletes it from the set"""
        result = self.__arb__()
        self.delete(result)
        return result

    def __fromB__(self):
        """:returns the first element from the set and deletes it."""
        result = self.first()
        self -= result
        return result

    def __fromE__(self):
        """:returns the last element from the set and deletes it."""
        result = self.last()
        self -= result
        return result

    def first(self):
        """:returns the first element from the set."""
        if self.tree.root is None:
            return None
        return self.tree.root.min().key

    def last(self):
        """:returns the last element from the set."""
        if self.tree.root is None:
            return None
        return self.tree.root.max().key

    def __str__(self):
        """:returns the string representation in the form of list of values in curly brackets separated by commas"""
        return "{" + ", ".join(("'" + str(i) + "'") if type(i) == str else str(i) for i in self) + "}"

    def __repr__(self):
        """string for internal string representation"""
        return str(self)

    def __add__(self, other):
        """Only two elements of type set or list can be joint to a union set. Otherwise it
        :raises a TypeError.
        Invoked by the + operator.

        :param other: The set to be joined with self
        :return: The joint set
        """
        if not isinstance(other, (list, Set)):
            raise TypeError("sets can only be joined with sets")
        new_set = self._clone()
        for element in other:
            new_set._insert(element)
        return new_set

    def __sub__(self, other):
        """Only two elements of type set or list can be subtracted from each other. Otherwise it
        :raises a TypeError.
        Invoked by the - operator.

        :param other: The set to be subtracted from self

        :return: the differene set of self and other
        """
        if not isinstance(other, (list, Set)):
            raise TypeError("only sets can be removed from sets")

        new_set = self._clone()

        for element in other:
            new_set.delete(element)

        return new_set

    def __mul__(self, other):
        """Computes intersection set between self and other. Invoked by the * operator.

        :param other: The set to intersect with self
        :return: Returns intersection set between self and other.
        """
        if not isinstance(other, (Set, list)):
            raise TypeError(f"could not intersect set and {type(other)}")

        return Set(x for x in other if x in self)

    def __mod__(self, other):
        """ computes the symmetric difference of two sets. Invoked by the % operator."""
        return (self - other) + (other - self)

    def __pow__(self, other):
        """Computes the cartesian product with itself if other is equal to 2.

        :raises a TypeError if other parameter is not 2.

        Invoked by the ** operator.
        """
        if other == 2:
            # cartesian product
            new_set = Set()
            for s1 in self:
                for s2 in self:
                    new_set += Set(List([[s1, s2]]))
            return new_set
        raise TypeError(
            f"{other} must be 2 to compute cartesian product of a set with itself")

    def power_set(self):
        """SetlX equivalent to 2** set. Computes the powerset of the set."""
        if self._is_empty():
            return Set([Set()])

        copy_set = self._clone()

        element = copy_set.__from__()

        power_set = copy_set.power_set()

        result = Set()

        for item in power_set:
            result += Set([Set([element]) + item]) + Set([item])
        return result

    def __eq__(self, other):
        """Determines if two sets are equal. Also works if tree is structured differently."""
        try:
            """Checks if other is not None. A check other == None would result in an endless loop. Therefore, this
            try-except block is necessary."""
            _ = other.tree
        except AttributeError:
            return False
        return self.tree == other.tree

    def __le__(self, other):
        """Checks if self is subset from other or equal."""
        if other is not None and self is not None:
            return self < other or self == other
        return False

    def __lt__(self, other):
        """Checks if self is subset from other."""
        if self.tree is None:
            return True
        if other is None or other.tree is None:
            return False

        if len(self) >= len(other):
            return False

        if self.tree is not None and other.tree is not None:
            for x in self:
                if x not in other:
                    return False
            return True
        return False

    def __gt__(self, other):
        """Implements > relation for sets.
        :returns other < self which is equal to self > other
        """
        return other < self

    def __ge__(self, other):
        """Implements >= relation for sets.

        :returns self >= other which is equal to other <= self
        """
        return other <= self

    def find(self, key):
        """:returns the key if it is in the set"""
        return self.tree.find(key)

    def delete(self, key):
        """Deletes the node with the
        :param key
        """
        self.tree.delete(key)

    def _insert(self, key):
        """Inserts an element with the
        :param key
        """
        self.tree.insert(key)

    def clear(self):
        """Returns an empty set."""
        self.tree = Tree()

    def __rnd__(self):
        """:returns a random element in the set."""
        rand_i = random.randint(0, len(self) - 1)
        for i, element in enumerate(self):
            if i == rand_i:
                return element

    def __domain__(self):
        """:returns a set of all keys if set is used as a map"""
        # if not self.tree.is_map:
        #     raise Exception(f"{self} is not a map")
        d = Set()
        for k in self:
            try:
                if len(k) == 2:
                    k = k[1]
            except TypeError:
                pass
            d += Set(k)

        return d

    def __range__(self):
        """:returns a set of all values if set is used as a map"""
        # if not self.tree.is_map:
        #     raise Exception(f"{self} is not a map")
        r = Set()
        for k in self:
            try:
                if len(k) == 2:
                    k = k[2]
                    r += Set(k)
            except TypeError:
                raise NotAMapError("%s is not a map." % str(self))
        return r

    def _is_empty(self):
        """:returns if the set does not contain any values"""
        return self.tree.total == 0

    def __hash__(self):
        """Makes set hashable."""
        size = self.tree.total
        _hash = size
        if size >= 1:
            _hash = size * 31 + hash(self.first())
            if size >= 2:
                _hash = _hash * 31 + hash(self.last())
        return _hash
