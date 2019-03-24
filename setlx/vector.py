from .native import isNumber


class Vector:
    def __init__(self, *args):
        self.values = [x for x in args]

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.values) != len(other):
                raise Exception(
                    "Vectors with different number of dimensions cannot be added to one another.")
            return Vector(*(x+y for (x, y) in zip(self.values, other)))
        raise Exception(f"Cannot add Vector and {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self.values) != len(other):
                raise Exception(
                    "Vectors with different number of dimensions cannot be subtracted to one another.")
            return Vector(*(x-y for (x, y) in zip(self.values, other)))
        raise Exception(f"Cannot subtract Vector and {type(other)}")

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.values) != len(other):
                raise Exception(
                    "Scalar product cannot be called with vectors with different number of dimensions.")
            return sum(x*y for (x, y) in zip(self.values, other))
        if isNumber(other):
            return Vector(*(other * x for x in self.values))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __cross__(self, other):
        if len(self.values) != 3 or len(other) != 3:
            raise Exception(
                "Vector product is only defined for 3 dimensional vectors.")
        a = self.values
        b = other
        return Vector(a[1]*b[2] - a[2]*b[1],
                      a[2]*b[0] - a[0]*b[2],
                      a[0]*b[1] - a[1]*b[0])

    def __iter__(self):
        return iter(self.values)

    def __len__(self):
        return len(self.values)

    def __eq__(self, value):
        return len(value) == len(self.values) and all(x == y for (x, y) in zip(self.values, value))

    def __ne__(self, value):
        return not(self.__eq__(value))

    def __getitem__(self, index):
        return self.values[index]

    def __setitem__(self, index, value):
        self.values[index] = value

    def __str__(self):
        return f"<<{' '.join([str(x) for x in self.values])}>>"

    def __repr__(self):
        return self.__str__()
