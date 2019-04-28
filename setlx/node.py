from setlx import list


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
        # stores key and value in the form setlx.List([key,value])
        self.key = key
        # self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        key, value = None, None
        if isinstance(self.key, list.List) and len(self.key) == 2:  # map feature is being used
            key = self.key[1]  # indices start at 1!
            value = self.key[2]
        else:
            key = self.key
        s = "" if value == None else f":{value}"
        return f"[{key}{s},{self.left},{self.right}]"

    def __repr__(self):
        return str(self)

    def __getitem__(self, key):
        results = []
        for node in self._traverse():
            if  key == node.key[1]:
                results.append(node)
            if len(results) > 1:
                return None
        if len(results) != 1:
            return None
        else:
            return results[0]
        # returns None if Node got no value

    # def _get_item_by_index(self, index):
    #     for i, node in enumerate(self._traverse()):
    #         if i == index:
    #             return node

    def insert(self, node):
        node_key = _Key(node.key)  # make keys comparable
        self_key = _Key(self.key)
        # if isinstance(self.key, list.List) and isinstance(node.key, list.List) and self_key == node_key:
        #     self.key[2] = node.key[2]  # indices start at 1
        #     return 0
        if node_key < self_key:
            # same effect as < operator but works for python sets as well
            if self.left != None:
                return self.left.insert(node)
            self.left = node
            return self, 1
        if node_key != self_key:
            if self.right != None:
                return self.right.insert(node)
            self.right = node
            return self, 1
        return self, 0

    def _find(self, key):
        k_key = _Key(key)
        self_key = _Key(self.key)
        if k_key == self_key:
            # TODO: discuss behavior of find
            return self.key
        if k_key < self_key and self.left != None:
            return self.left._find(key)
        if k_key > self_key and self.right != None:
            return self.right._find(key)
        # TODO: raise error

    def delete(self, key):
        """
        Deletes the parameter key from the set
        """
        parent = self
        k_key = _Key(key)
        parent_key = _Key(parent.key)

        if parent.left is not None and k_key < parent_key:
            to_delete = parent.left
            if _Key(to_delete.key) == k_key:
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
        elif parent.right is not None and k_key > parent_key:
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

    def max(self):
        """ returns node with min key"""
        if self.right == None:
            return self
        else:
            return self.right.max()

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
