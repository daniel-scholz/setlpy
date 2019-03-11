from setlx.node import BinaryNode


class Tree():
    def __init__(self, node=None):
        self.root = None
        self.total = 0
        if node != None:
            self.insert(node)  # ensures that total count is correct
    """Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.(https://www.programiz.com/python-programming/iterator)"""

    def __iter__(self):
        """
        returns the iterator object
        """
        self.current_node = self[0]
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.total:
            self.current_node = self.__getitem__(index=self.index)
            self.index += 1
            return self.current_node
        else:
            raise StopIteration

    def __getitem__(self, index):
        if index < 0:
            index = self.total - abs(index)
        return self.root.__getitem__(index)

    def insert(self, node):
        if not isinstance(node, BinaryNode):
            node = BinaryNode(node)
        if self.root == None:
            self.root = node
        else:
            self.root.insert(node)
        self.total += 1

    def _find(self, key):
        if self.root != None:
            return self.root._find(key)

    # extracts key from nnode
    def find(self, key):
        return self._find(key).key

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
                        # parent.key = current.del_min()
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
        return "{}"

    def __eq__(self, other):
        if self.root != None:
            return self.root == other.root
        else:  # elif other == None:
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
        #root_eq = other.find(self.root.key)
        for node in self._traverse():
            # print(node)
            if not other.find(node.key):
                return False
        return True

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
