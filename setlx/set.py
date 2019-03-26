from setlx.tree import Tree
from setlx.node import BinaryNode


class Set():
    # https://stackoverflow.com/questions/19151/build-a-basic-python-iterator
    def __init__(self, arg=None):
        if isinstance(arg, Tree):
            self.tree = arg
        elif isinstance(arg, BinaryNode) or isinstance(arg, int) or arg == None:
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
        item = self.tree.__getitem__(index)
        return item.key if isinstance(item, BinaryNode) else item

    def __len__(self):
        return self.tree.total

    def __from__(self):
        # look up SetlX implementation
        return self[0]

    def first(self):
        return self[0]

    def last(self):
        return self[-1]

    def __str__(self):
        return "{" + ", ".join(str(self[i]) for i in range(0, self.tree.total))+"}"

    def __repr__(self):
        return self.__str__()

    """https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types"""

    def __add__(self, other):
        if isinstance(other, int):
            self.tree.insert(other)
        else:
            try:
                others = iter(other)  # raises TypeError if not castable
                for o in others:
                    self.tree.insert(o)
            except (TypeError):
                raise TypeError(
                    f"items of type {type(other)} cannot be add to set")
            # raise NotImplementedError()
        return self

    def __sub__(self, other):
        if isinstance(other, int):
            self.tree.delete(other)
        else:
            try:
                others = iter(other)  # raises TypeError if not castable
                for o in others:
                    if o in self:
                        self.tree.delete(o)
            except (TypeError):
                raise TypeError(
                    f"items of type {type(other)} cannot be removed from set")
            # raise NotImplementedError()
        return self

    def __mul__(self, other):
        pass

    def __matmul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __pow__(self, other, modulo=None):
        pass

    def __and__(self, other):
        pass

    def __xor__(self, other):
        pass

    def __or__(self, other):
        pass


def arb(s):
    try:
        return s.__arb__()
    except:
        raise Exception(f"arb not defined on type {type(s)}")
