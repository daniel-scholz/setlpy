from setlx.node import BinaryNode


class Tree():
    def __init__(self, key=None, value=None):
        self.root = None
        self.total = 0
        if key != None:
            self.insert(key, value)  # ensures that total count is correct
    """Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.(https://www.programiz.com/python-programming/iterator)"""

    def __iter__(self):
        """
        returns the iterator object
        """
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.total:
            old_i = self.index
            self.index += 1
            node = self.root._get_item_by_index(old_i)
            if node.value != None:
                return node.key, node.value
            else:
                return node.key
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.root[key]

    def __setitem__(self, key, value):
        self.insert(BinaryNode(key, value))

    def _clone(self):
        new_tree = Tree()
        for node in self:
            if isinstance(node, tuple):
                new_tree.insert(node[0], node[1])
            else:
                new_tree.insert(node)
        return new_tree

    def insert(self, key, value=None):
        node = BinaryNode(key, value) if not isinstance(
            key, BinaryNode) else key
        if self.root == None:
            self.root = node
            self.total += 1
        else:
            self.total += self.root.insert(node)

    def find(self, key):
        return self.root._find(key) if self.root != None else None

    def delete(self, key):
        if isinstance(key,BinaryNode):
            key = key.key
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

        else:
            raise ValueError(f"tree is empty")

    # def min(self):
    #     """ returns node with min key"""
    #     if self.root != None:
    #         if self.root.left == None:
    #             return self.root
    #         else:
    #             return self.root.min()
    #     raise ValueError(f"tree is empty")

    def __str__(self):
        if self.root != None:
            return str(self.root)
        return "[]"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if other == None:
            return False
        if self.root != None or other.root != None:
            return self.root == other.root
        else:  # elif other == None:
            if self.root == None and other.root == None:
                return True
            return False

    def _traverse(self):
        # https://stackoverflow.com/questions/8991840/recursion-using-yield
        # yield self.root
        yield from self.root._traverse()

    def __le__(self, other):  # a.k.a. is_subset
        """
        corresponds to self <= other
        implements check for subset, NOT real less or equal
        other is subset of self; all elements of self are in other
        """
        if self.root == None:  # left set is empty
            return True
        if other.root == None and self.root != None:  # right set is empty
            return False

        if other.root != None and self.root != None:
            for node in self:
                if other.find(node) == None:
                    return False
            return True

    def __lt__(self, other):
        """
        implements check for real subset, NOT real less
        """
        return not self.__eq__(other) and self.__le__(other)

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
