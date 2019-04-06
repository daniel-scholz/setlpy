
class List(list):
    def __getitem__(self, index):
        if isinstance(index, slice):
            start = index.start and index.start-1
            index = slice(start, index.stop, index.step)
        else:
            index -= 1
        return super().__getitem__(index)

    def __setitem__(self, key, value):
        return super().__setitem__(key-1, value)
