from copy import deepcopy


class List(list):
    """ A list that starts with index one instead of zero"""
    def __getitem__(self, index):
        if isinstance(index, slice):
            if index.start == 0:
                raise Exception(f"Lower bound '{index.start}' is invalid.")
            start = index.start
            if start != None and start > 0:
                start -= 1
            stop = index.stop
            if stop != None:
                if stop == -1:
                    stop == None
                elif stop < 0:
                    stop += 1
            index = slice(start, stop, index.step)
            result = List(deepcopy(super().__getitem__(index)))
            return result
        else:
            if index == 0 or index > len(self):
                return None
            if index > 0:
                index -= 1
            return super().__getitem__(index)

    def __setitem__(self, key, value):
        if key == 0:
            return
        length = len(self)
        if key < 0:
            key = length - key
        if key - 1 >= length:
            self += [None for _ in range(key-length)]
        return super().__setitem__(key-1, deepcopy(value))

    def __add__(self, other):
        result = super().__add__(list(other))
        return List(deepcopy(result))

    def __mul__(self,other):
        result = super().__mul__(other)
        return List(deepcopy(result))

    def __hash__(self):
        return hash(str(self))
