from functools import reduce

from .utils import is_number, is_integer
from .vector import Vector


class Matrix:
    def __init__(self, values):
        if len(values) == 0:
            raise Exception("Cannot create empty matrix.")
        elif len(values) > 1:
            # check if all vectors have same size
            last = len(values[0])
            for vec in values[1:]:
                if len(vec) != last:
                    raise Exception(
                        "Cannot create matrix from vectors of different sizes")
                last = len(vec)
        self.values = [Vector(*v) for v in values]

    def to_list(self):
        return [v.to_list() for v in self.values]

    def __add__(self, other):
        if isinstance(other, Matrix):
            if dim(self) != dim(other):
                raise Exception(
                    "Matrices with different dimensions cannot be added to one another.")
            return Matrix([x.__add__(y).to_list() for (x, y) in zip(self.values, other)])
        raise Exception(f"Cannot add Matrix and {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if dim(self) != dim(other):
                raise Exception(
                    "Matrices with different dimensions cannot be subtracted to one another.")
            return Matrix([x.__sub__(y).to_list() for (x, y) in zip(self.values, other)])
        raise Exception(f"Cannot subtract Matrix and {type(other)}")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if dim(self)[1] != dim(other)[0]:
                raise Exception(
                    "Matrix multiplication is only defined if the number of columns of the first matrix equals the number of rows of the second matrix.")
            # Matrix multiplication

            zip_b = zip(*other.to_list())
            zip_b = list(zip_b)
            return Matrix([[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
                            for col_b in zip_b] for row_a in self.to_list()])
        if is_number(other):
            return Matrix([x.__mul__(other).values for x in self.values])
        raise Exception(f"Cannot multiply Matrix and {type(other)}")

    def __pow__(self, other):
        if not is_integer(other) or (isinstance(other, Matrix) and dim(other)[0] != dim(other)[1]):
            raise Exception("Power is only defined on square matrices.")

        if other < 0:
            # TODO calculate inverse
            raise Exception("Inverting matrix is not supported")
        return other * self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __dim__(self):
        return (len(self.values), len(self.values[0]))

    def __iter__(self):
        return iter(self.values)

    def __len__(self):
        return len(self.values)

    def __eq__(self, value):
        return isinstance(value, Matrix) and dim(value) == dim(self) and all(x == y for (x, y) in zip(self.values, value))

    def __ne__(self, value):
        return not(self.__eq__(value))

    def __getitem__(self, index):
        return self.values[index]

    def __setitem__(self, index, value):
        self.values[index] = value

    def __str__(self):
        return f"<< {' '.join([str(x) for x in self.values])} >>"

    def __repr__(self):
        return self.__str__()

    def to_vector(self):
        d = dim(self)
        if d[0] == 1:
            return Vector(self.values[0].to_list())  # copy vector
        if d[1] == 1:
            return Vector([x[0] for x in self.values])
        raise Exception(
            "Matrix could not be converted to a vector, because it doesn't have just one column or just one row.")


def dim(matrix):
    return matrix.__dim__()
