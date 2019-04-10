from itertools import product as _product
from functools import reduce


def cartesian_product(*iterables):
    # TODO enable overriding for vectors and matrices
    return _product(*[tuple(i) for i in iterables])


_sum = sum


def sum(iterable, default=None):
    if len(iterable) == 0:
        return default
    return reduce(lambda x, y: x+y, iterable) or default


def product(iterable, default=None):
    p = 1
    for i in iterable:
        p *= i
    return p or default


def map(value):
    if value == None:
        return set()


def _range(start, end, step=1):
    offset = +1 if end >= start else -1
    return range(start, end+offset, step)
