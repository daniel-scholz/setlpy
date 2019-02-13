from functools import lru_cache as _lru_cache
from inspect import getfullargspec
from copy import deepcopy as _deepcopy

class cached_procedure:
    def __init__(self, fn):
        self.fn = fn
        self.decorator = _lru_cache(maxsize=None, typed=False)(fn)

    def __call__(self, *args, **kwargs):
        # no read/write arguments in cached procedures!
        args = [_deepcopy(a) for a in args]
        kwargs = {name: _deepcopy(value) for name, value in kwargs.items()}
        return self.decorator(*args, **kwargs)


class procedure:
    def __init__(self, fn):
        self.fn = fn
        self.arg_info = getfullargspec(fn)

    def __call__(self, *args, **kwargs):
        arg_info = self.arg_info
        ants = arg_info.annotations

        args_cp = []
        for i, a in enumerate(args):
            arg_name = arg_info.args[i]
            # only copy value if argument hast read/write annotation
            if arg_name in ants and ants[arg_name] == "rw":
                args_cp.append(a)
            else:
                args_cp.append(_deepcopy(a))

        # arguments which are assigned by name (e.g. x=2)
        kwargs_cp = {}
        for arg_name, value in kwargs.items():
            # only copy value if argument hast read/write annotation
            if arg_name in ants and ants[arg_name] == "rw":
                kwargs_cp[arg_name] = value
            else:
                kwargs_cp[arg_name] = _deepcopy(value)

        return self.fn(*args_cp, **kwargs_cp)

