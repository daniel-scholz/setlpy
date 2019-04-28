from setlx.node import BinaryNode
from setlx.list import List

import copy


class Tree:
    def __init__(self, key=None):
        self.root = None
        self.total = 0
        self.is_map = False
        self.parents = {}
        self.current = None
        if key != None:
            self.insert(key)  # ensures that total count is correct
    """Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), 
    collectively called the iterator protocol.(https://www.programiz.com/python-programming/iterator) """

    def __iter__(self):
        """
        returns the iterator object
        """
        new_tree = self._clone()
        new_tree.iterator = self._traverse()
        new_tree.current = self.root.min()
        return new_tree

    def __next__(self):
        element = self.iterator.__next__()
        return element

    """ functions to implement map feature"""

    def __getitem__(self, key):
        if not self.is_map:
            return None
        return self.root[key]

    def __setitem__(self, key, value):
        if not self.is_map:
            return
        for item in self:
            if item != None and item.key[1] == key:
                self.delete(item.key)

        self.insert(List([key, value]))
    """"""

    def _clone(self):
        return copy.deepcopy(self)
        # new_tree = Tree()
        # new_tree.root = self.root
        # new_tree.total = self.total
        # return new_tree

    def insert(self, key):

        node = BinaryNode(key) if not isinstance(
            key, BinaryNode) else key  # checks if insert is called from splaynode class
        if isinstance(node.key, list) and len(node.key) == 2:
            self.is_map = True
        else:
            # flag needs to be set on false when non map element is inserted
            self.is_map = False
        if self.root == None:
            self.root = node
            self.total += 1
            self.parents[str(node.key)] = None

        else:
            try:
                parent, result = self.root.insert(node)
                self.total += result
                self.parents[str(node.key)] = copy.deepcopy(parent)
            except Exception as e:
                raise Exception(
                    f"node {key} could not be inserted due to >>{e}<<")

    def find(self, key):
        return self.root._find(key) if self.root != None else None

    def delete(self, key):
        tree = self
        if tree.root != None:
            root = tree.root
            if root.key == key:
                # check if right subtree i  s minimum
                if root.right == None:
                    tree.root = root.left
                elif root.left == None:
                    tree.root = root.right
                else:
                    root_right = root.right
                    if root_right.left == None:
                        root.right = root_right.right
                        root.key = root_right.key
                    else:
                        root.key = root_right.del_min()
            else:
                tree.root.delete(key)
            self.total -= 1
        

    def __str__(self):
        if self.root != None:
            return str(self.root)
        return "[]"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if other == None:
            return False
        return self._compare_to(other) == 0
        # if other == None:
        #     return False
        # if self.root != None or other.root != None:
        #     return self.root == other.root
        # else:  # elif other == None:
        #     if self.root == None and other.root == None:
        #         return True
        #     return False

    def _traverse(self):
        # https://stackoverflow.com/questions/8991840/recursion-using-yield
        # yield self.root
        if self.root == None:
            return None
        yield from self.root._traverse()

    def __le__(self, other):  # a.k.a. is_subset
        """
        corresponds to self <= other
        implements check for subset, NOT real less or equal
        other is subset of self; all elements of self are in other
        """
        return self.__eq__(other) or self.__lt__(other)

    def __lt__(self, other):
        """
        implements check for real subset, NOT real less
        """
        if self.root == None:  # left set is empty
            return True
        if other.root == None:  # and self.root != None:  # right set is empty and left set is not
            return False
        if other.root != None and self.root != None:
            for self_node, other_node in zip(self, other):
                if self_node == other_node:
                    continue
                return self_node < other_node
            if self.total < other.total:  # which one has more elements
                return True
        return False

    def __gt__(self, other):
        """
        returns self > other
        """
        return other.__lt__(self)

    def __ge__(self, other):
        """
        returns self >= other
        """
        return other.__le__(self)

    def _compare_to(self, other):  # 1 => self < other
        if self.root == None:  # left set is empty
            return 1
        if other.root == None:  # and self.root != None:  # right set is empty and left set is not
            return -1
        if other.root != None and self.root != None:
            for self_node, other_node in zip(self, other):
                if self_node.key == other_node.key:
                    continue
                return 1 if self_node < other_node else -1
            if self.total < other.total:  # which one has more elements
                return 1
            return 0
        return 0
