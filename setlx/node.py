class _Key():
    """
    class for elements in a Node of a BinaryTree
    """

    def __init__(self, key):
        if type(key) == _Key:  # prevent nested keys
            self.key = key.key
        else:
            self.key = key

    def __eq__(self, other):
        if not isinstance(other, _Key):
            other = _Key(other)
        return self.key == other.key

    def __le__(self, other):
        if type(self.key) == type(other.key):
            return self.key <= other.key
        return str(type(self.key)) <= str(type(other.key))

    def __lt__(self, other):
        if not isinstance(other, _Key):
            other = _Key(other)
        return self.key != other.key and self <= other

    def __gt__(self, other):
        """
        returns self > other
        """
        if not isinstance(other, _Key):
            other = _Key(other)
        return other < self

    def __ge__(self, other):
        """
        returns self >= other
        """
        if not isinstance(other, _Key):
            other = _Key(other)
        return other <= self

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self)


class BinaryNode():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return f"[{self.key},{self.left},{self.right}]"

    def __getitem__(self, index):
        for i, item in enumerate(self._traverse()):
            if i == index:
                return item
        raise IndexError

    def insert(self, node):
        if _Key(node.key) > _Key(self.key):
            if self.right != None:
                return self.right.insert(node)
            self.right = node
            return 1
        # similar effect to < operator but works for python sets as well
        elif _Key(node.key) != _Key(self.key):
            if self.left != None:
                return self.left.insert(node)
            self.left = node
            return 1
        return 0

    def _find(self, key):
        if not isinstance(key, _Key):
            key = _Key(key)
        if _Key(key) == _Key(self.key):
            return self
        if _Key(key) < _Key(self.key) and self.left != None:
            return self.left._find(key)
        if _Key(key) > _Key(self.key) and self.right != None:
            return self.right._find(key)
        # TODO: consider raising an error
    def delete(self, key):
        """
        Deletes the parameter key from the set
        """
        parent = self
        if parent.left != None and _Key(key) < _Key(parent.key):
            to_delete = parent.left
            if _Key(to_delete.key) == _Key(key):
                if to_delete.right == None:
                    parent.left = to_delete.left
                elif to_delete.left == None:
                    parent.left = to_delete.right
                else:
                    to_delete_child = to_delete.right
                    if to_delete_child.left == None:
                        to_delete.right = to_delete_child.right
                        to_delete.key = to_delete_child.key
                    else:
                        to_delete.key = to_delete_child.del_min()
                    # current.key = parent.del_min()
            else:
                to_delete.delete(key)
        elif parent.right and key > parent.key:
            to_delete = parent.right
            if _Key(to_delete.key) == _Key(key):
                if to_delete.right == None:
                    parent.right = to_delete.left
                elif to_delete.left == None:
                    parent.right = to_delete.right
                else:
                    to_delete_child = to_delete.right
                    if to_delete_child.left == None:
                        to_delete.right = to_delete_child.right
                        to_delete.key = to_delete_child.key
                    else:
                        to_delete.key = to_delete_child.del_min()
                    # current.key = parent.del_min()
            else:
                to_delete.delete(key)
        else:
            raise ValueError(f"could not delete {key}")

    def del_min(self):
        """
            Returns value of minimum of subtree self
            Deletes node of minimum value
        """
        start_node = self
        potential_min = start_node.left
        if potential_min.left == None:
            k = potential_min.key
            start_node.left = potential_min.right
            return k
        else:
            return potential_min.del_min()

    def min(self):
        """ returns node with min key"""
        if self.left == None:
            return self
        else:
            return self.left.min()

    def __eq__(self, other):
        o_none, s_none = False, False
        try:  # if other == None
            _ = other.key
        except AttributeError:
            o_none = True  # other == None
        try:  # if self == None
            _ = self.key
        except AttributeError:
            s_none = True  # self == None

        if not s_none and not o_none:
            key___eq = self.key == other.key
            left__eq = self.left == other.left
            right_eq = self.right == other.right
            return key___eq and left__eq and right_eq

        return o_none and s_none

    def __le__(self, other):
        return _Key(self.key) <= _Key(other.key)

    def __lt__(self, other):
        return _Key(self.key) < _Key(other.key)

    def __gt__(self, other):
        return _Key(self.key) > _Key(other.key)

    def __ge__(self, other):
        return _Key(self.key) >= _Key(other.key)

    def _traverse(self):
        if self.left != None:
            yield from self.left._traverse()
        yield self
        if self.right != None:
            yield from self.right._traverse()
