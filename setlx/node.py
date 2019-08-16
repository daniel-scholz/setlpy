from types import GeneratorType


class NotAMapError(Exception):
    pass


class _Key:
    """This class provides the possibility to compare objects of any type with each other by comparing the string of the
    type name if they are different, else the usual comparison operation between both objects are invoked.
    """
    @staticmethod
    def _compare_to(first, second):
        """Compares two sets lexicographically. the i-th element of each set is compared. Once the two elements differ
        the outcome is determined by which of the two elements is greater.

        :param other: The other tree (set) which should be compared to self.
        :return: 1 if self < other, 0 self == other, -1 self > other
        """
        if first is None and second is None:
            return 0
        if first is None:  # left set is empty
            return 1
        if second is None:  # right set is empty and left set is not
            return - 1

        if second is not None and first is not None:
            for f, s in zip(first, second):
                if f == s:
                    continue
                return 1 if _Key(f) < _Key(s) else -1
            if len(first) < len(second):  # which one has more elements
                return 1
            if len(first) > len(second):  # which one has more elements
                return -1
        return 0

    def __init__(self, key):
        if type(key) == _Key:  # prevent nested keys in recursive calls
            self.key = key.key
        else:
            self.key = key

    def __eq__(self, other):
        if isinstance(self.key, type(other.key)):
            if isinstance(self.key, str):
                return self.key == other.key
            try:
                return _Key._compare_to(self.key, other.key) == 0
            except TypeError:
                return self.key == other.key
        return str(type(self.key)) == str(type(other.key))

    def __le__(self, other):
        if isinstance(self.key, type(other.key)):
            try:
                if isinstance(self.key, str):
                    return self.key <= other.key
                comp_res = _Key._compare_to(self.key, other.key)
                return comp_res == 1 or comp_res == 0
            except TypeError:
                return self.key <= other.key
        return str(type(self.key)) < str(type(other.key)) or str(type(self.key)) == str(type(other.key))

    def __lt__(self, other):
        if isinstance(self.key, type(other.key)):
            try:
                if isinstance(self.key, str):
                    return self.key <= other.key
                comp_res = _Key._compare_to(self.key, other.key)
                return comp_res == 1
            except TypeError:
                return self.key < other.key
        return str(type(self.key)) < str(type(other.key))

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


class Node:
    """This class represents one node in a ordered binary search tree."""

    def __init__(self, key, left=None, right=None):
        """

        :param key: The key of the Node. Might also be a List of length, which is equal to (key,value)-pair
        :param left: The left child node of self. Also of type Node
        :param right: The left child node of self. Also of type Node
        """
        self.key = key  # stores key and value in the form setlx.List([key,value])
        self.left = left
        self.right = right

    def __str__(self):
        """:returns string output for a node. different outputs for maps or sets"""
        key, value = None, None
        if isinstance(self.key, list.List) and len(self.key) == 2:  # map feature is being used
            key = self.key[1]  # indices start at 1!
            value = self.key[2]
        else:
            key = self.key
        s = "" if value is None else f":{value}"
        return f"[{key}{s},{self.left},{self.right}]"

    def __repr__(self):
        return str(self)

    def __getitem__(self, key):
        """
        :return: Corresponding key for value. None if the set does not represent a functional relation
        """
        results = []
        for node in self.traverse_key(key):
            try:
                l = len(node.key)
                if node.key == key or(l == 1 and key == node.key[1]):
                    """Case: Single element in set."""
                    return None
                if l == 2 and key == node.key[1]:
                    """Only case, where a map applies."""
                    results.append(node)
                if l > 2:
                    raise NotAMapError("".join((str(self), "is not a map.")))
                if len(results) > 1:
                    return None
            except TypeError:
                """Case: Element is no iterable type, hence no item can be found."""
                continue
        return results[0] if len(results) == 1 else None

    def insert(self, node, handle_map=False):
        """Inserts an object of type Node into the Tree.

        :param node: Instance of the node class passed from class Tree
        :return: 1 if insertion was successful, 0 if element already exists in tree
        """
        # make keys comparable
        node_key = _Key(node.key)
        self_key = _Key(self.key)

        if handle_map:
            k_self = self.key[1]
            k_node = node.key[1]
            if k_self == k_node:
                self.key[2] = node.key[2]
                return 0

        # if node_key == self_key:
        #     self.key = node.key
        #     return 0

        if node_key < self_key:
            if self.left is not None:
                return self.left.insert(node)
            self.left = node
            return 1

        if node_key != self_key:
            """unequal operator is used, because for some types (e.g. python sets)
             the length of an object is used for greater comparison.
            """
            if self.right is not None:
                return self.right.insert(node)
            self.right = node
            return 1
        return 0

    def find(self, key):
        """Recursive implementation of find. returns the key if it is found, else None"""
        k_key = _Key(key)
        self_key = _Key(self.key)
        if k_key == self_key:
            return self.key
        if k_key < self_key and self.left is not None:
            return self.left.find(key)
        if k_key > self_key and self.right is not None:
            return self.right.find(key)

    def delete(self, key):
        """Deletes key from tree, updates self.total and restores order of tree.

        """
        parent = self  # for clarification reasons. This is not the node which should be deleted.
        k_key = _Key(key)
        parent_key = _Key(parent.key)

        if parent.left is not None and k_key < parent_key:
            """determine if the key which should be deleted is in left or right subtree."""
            to_delete = parent.left  # the node which should be deleted.
            if _Key(to_delete.key) == k_key:
                if to_delete.right is None:
                    # szenario 1: right subtree is empty
                    parent.left = to_delete.left
                elif to_delete.left is None:
                    # szenario 2: left subtree is empty
                    parent.left = to_delete.right
                else:
                    # szenario 3: both subtrees are not empty
                    to_delete_child = to_delete.right
                    if to_delete_child.left is None:
                        to_delete.right = to_delete_child.right
                        to_delete.key = to_delete_child.key
                    else:
                        to_delete.key = to_delete_child.del_min()
            else:
                to_delete.delete(key)
        elif parent.right is not None and k_key > parent_key:
            to_delete = parent.right
            if _Key(to_delete.key) == _Key(key):
                if to_delete.right is None:
                    # szenario 1: right subtree is empty
                    parent.right = to_delete.left
                elif to_delete.left is None:
                    # szenario 2: left subtree is empty
                    parent.right = to_delete.right
                else:
                    # szenario 3: both subtrees are not empty
                    to_delete_child = to_delete.right
                    if to_delete_child.left is None:
                        to_delete.right = to_delete_child.right
                        to_delete.key = to_delete_child.key
                    else:
                        to_delete.key = to_delete_child.del_min()
            else:
                to_delete.delete(key)
        # else:
        #    raise ValueError(f"could not delete {key}")

    def del_min(self):
        """
            :returns value of minimum of subtree self
                Deletes node of minimum value
        """
        start_node = self
        potential_min = start_node.left
        if potential_min.left is None:
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
        """ returns node with max key"""
        if self.right is None:
            return self
        else:
            return self.right.max()

    def __eq__(self, other):
        """:returns if two nodes are equal. Two nodes are only equal if the key and both subtrees are the same"""

        o_none, s_none = False, False
        """This try except method is used because checking other == None would result in an endless loop."""
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

    def traverse_key(self, key):
        """Traverses the tree from the node downwards. This used for searching a key. Only the elements which are relevant are visited. 
         The elements are yielded in ascending order.
        """
        s_key = _Key(self)
        k_key = _Key(key)

        if k_key < s_key and self.left is not None:
            yield from self.left.traverse_key(k_key)
        yield self
        if k_key > s_key and self.right is not None:
            yield from self.right.traverse_key(k_key)

    def traverse(self):
        """Traverses the tree from the node downwards. Each element is yielded on the __next__ call on the returned
        generator. The elements are yielded in ascending order.
        """
        if self.left is not None:
            yield from self.left.traverse()
        yield self
        if self.right is not None:
            yield from self.right.traverse()
