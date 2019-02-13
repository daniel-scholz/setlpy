from itertools import product as _product


def cartesian_product(*iterables):
    return _product(iterables)


_sum = sum


def sum(iterable):
    return _sum(iterable)


def product(iterable):
    p = 1
    for i in iterable:
        p*=i
    return p
