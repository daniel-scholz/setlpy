from itertools import product as _product


def cartesian_product(*iterables):
    # TODO enable overriding for vectors and matrices
    return _product(*[tuple(i) for i in iterables])


_sum = sum


def sum(iterable):
    return _sum(iterable)


def product(iterable):
    p = 1
    for i in iterable:
        p *= i
    return p


def map(value):
    if value == None:
        return set()


def _range(start, end, step=1):
    offset = +1 if end > start else -1
    return list(range(start, end+offset, step))
