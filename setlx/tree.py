import copy

from setlx.list import List
from setlx.node import Node


class Tree:
    """
    This class provides the internal data structure in the form of ordered binary trees for the sets of the
    setlx-Module.
    """

    def __init__(self, key=None):
        """Constructor of this class. Initializes the root of the tree, the total amount of nodes in the tree and if it
        is used as map.

        Afterwards the the key is inserted by calling the insert function in order to ensure that the total count is
        correct.

        :param key: The tree is initialized with these element(s).
        """
        self.iterator = None
        self.root = None
        self.total = 0
        # self.is_map = False
        if key is not None:
            self.insert(key)  # ensures that total count is correct

    def __iter__(self):
        """The iterator attribute is initialized. It stores a generator object which yields a Node every time the next
        function is called on it.

        :returns A clone of the current tree to enable nested iterations over the same object.
        """

        new_tree = self._clone()
        new_tree.iterator = self.traverse()
        return new_tree

    def __next__(self):
        """Returns the next element in the tree by yielding the next element from the iterator."""

        if self.iterator == None:
            self.iterator = self.traverse()

        return self.iterator.__next__()

    """  The following two functions are implemented to provide the map feature"""

    def __getitem__(self, key):
        # if not self.is_map:
        #     return None
        return self.root[key]

    def __setitem__(self, key, value):
        # if not self.is_map:
        #     return
        for item in self.traverse_key(key):
            if item is not None and item.key[1] == key:
                self.delete(item.key)

        self.insert(List([key, value]))

    """"""

    def _clone(self):
        """:returns a copy of the current tree.
        Copies elementwise to avoid deepcopying generator object self.iterator"""

        new_tree = Tree()
        new_tree.root = copy.deepcopy(self.root)
        # new_tree.is_map = copy.deepcopy(self.is_map)
        new_tree.total = copy.deepcopy(self.total)
        # reset iterator
        new_tree.iterator = None
        return new_tree

    def insert(self, key):
        """Inserts new node into tree while incrementing the total count, to keep track of the total elements in the tree.

        :param key: The key to be inserted.
        :return: None. But the counter variable self.total is incremented.
        """
        node = Node(key) if not isinstance(
            key, Node) else key  # checks if insert is called from splaynode class
        if isinstance(node.key, list) and len(node.key) == 2:
            # flag needs to be set to True when map element is inserted
            # self.is_map = True
            pass
        else:
            # flag needs to be set to False when non map element is inserted
            # self.is_map = False
            pass
        if self.root is None:
            # Inserted element becomes root
            self.root = node
            self.total += 1

        else:
            # try:
            # result = self.root.insert(node, handle_map=self.is_map)
            result = self.root.insert(node)

            self.total += result
        # except Exception as e:
        #  raise Exception(
        #     f"node {key} could not be inserted due to >>{e}<<")

    def find(self, key):
        """:returns key when key was found and tree is not empty else None is returned."""
        return self.root.find(key) if self.root is not None else None

    def delete(self, key):
        """Deletes key from tree, updates self.total and restores order of tree.

        :param key: that is deleted
        :return: None
        """
        tree = self
        if tree.root is not None:
            root = tree.root
            if root.key == key:
                # check if right subtree is minimum
                if root.right is None:
                    tree.root = root.left
                elif root.left is None:
                    tree.root = root.right
                else:
                    root_right = root.right
                    if root_right.left is None:
                        root.right = root_right.right
                        root.key = root_right.key
                    else:
                        root.key = root_right.del_min()
            else:
                tree.root.delete(key)
            self.total -= 1

    def __str__(self):
        """:returns external string representation."""
        if self.root is not None:
            return str(self.root)
        return "[]"

    def __repr__(self):
        """:returns internal string representation"""
        return str(self)

    def __eq__(self, other):
        """:returns if to trees are equal."""
        if other is None:
            return False
        return self._compare_to(other) == 0

    def traverse(self):
        """starts traversing the tree from the root downwards. """
        if self.root is None:
            return None
        yield from self.root.traverse()

    def traverse_key(self, key):
        """starts traversing the tree from the root downwards. """
        if self.root is None:
            return None
        yield from self.root.traverse_key(key)

    def __le__(self, other):  # a.k.a. is_subset
        """:returns if the sets are equal or self < other"""
        return self.__eq__(other) or self.__lt__(other)

    def __lt__(self, other):
        """:returns if the elements of the set are lexicographically smaller than the one in other"""
        return self._compare_to(other) == 1

    def __gt__(self, other):
        """:returns self > other """
        return other.__lt__(self)

    def __ge__(self, other):
        """:returns self >= other
        """
        return other.__le__(self)

    def _compare_to(self, other):
        """Compares two sets lexicographically. the i-th element of each set is compared. Once the two elements differ
        the outcome is determined by which of the two elements is greater.

        :param other: The other tree (set) which should be compared to self.
        :return: 1 if self < other, 0 self == other, -1 self > other
        """
        if self.root is None and other.root is None:
            return 0
        if self.root is None:  # left set is empty
            return 1
        if other.root is None:  # right set is empty and left set is not
            return - 1

        if other.root is not None and self.root is not None:
            for self_node, other_node in zip(self, other):
                if self_node.key == other_node.key:
                    continue
                return 1 if self_node < other_node else -1
            if self.total < other.total:  # which one has more elements
                return 1
            elif self.total > other.total:
                return -1
            return 0
        return 0
