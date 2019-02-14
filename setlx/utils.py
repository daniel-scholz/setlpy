from itertools import product


def to_bool(value):
    """
    converts any value to a boolean
    TODO: check how setlx converts values to booleans
    """
    return bool(value)


def cartesian(v1, v2):
    type_v1 = type(v1)
    type_v2 = type(v2)
    if type_v1 != type_v2:
        raise f"cannot compute cartesian product for {type_v1} and {type_v2}"

    if type_v1 is list:
        if len(v1) != len(v2):
            raise "both lists must have same size"
        return [[x, v2[i]] for i, x in enumerate(v1)]

    # TODO for sets

    raise f"cannot compute cartesian product for type {type_v1}"


def iterate(**iterables):
    """
    TODO: maybe own implementation?
    """
    return product(iterables)


def _range(start, end, step):
    return list(range(start, end+1, step))
