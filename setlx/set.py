from setlx.tree import Tree
from setlx.node import BinaryNode


class Set():
    # https://stackoverflow.com/questions/19151/build-a-basic-python-iterator
    def __init__(self, arg=None):
        if isinstance(arg, Tree):
            self.tree = arg
        elif isinstance(arg, BinaryNode):
            self.tree = Tree(arg)
        else:
            # try:
                """
                check if argument for constructor is an iterable like list, set etc.
                """
                self.tree = Tree()
                for element in iter(arg):
                    print(self.tree, element)
                    self.tree.insert(element)
            # except TypeError:
            #     raise TypeError(
            #         f"set cannot be created from {type(arg)}")

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
        s = {self[i] for i in range(0, self.tree.total)}
        return f"{s}"


def arb(s):
    try:
        return s.__arb__()
    except:
        raise Exception(f"arb not defined on type {type(s)}")
