from functools import lru_cache as _lru_cache
from inspect import getfullargspec
from copy import deepcopy as _deepcopy


class cached_procedure:
    def __init__(self, func):
        self.cache = _lru_cache(maxsize=None, typed=False)(func)
        arg_info = getfullargspec(func)

        def decorator(*args, **kwargs):
            arg_names = arg_info.args
            if len(arg_names) > 0 and arg_names[0] == "self":
                arg_names = arg_names[1:]
            # no read/write arguments in cached procedures!
            c_args = (_deepcopy(a) if arg_info.args[i] !=
                    "self" else a for i, a in enumerate(args))
            c_kwargs = {name: _deepcopy(value) for name, value in kwargs.items()}
            return self.cache(*c_args, **c_kwargs)

        self.decorator = decorator
    
    def __call__(self, *args, **kwargs):
        return self.decorator(*args,**kwargs)



def procedure(func):
    arg_info = getfullargspec(func)

    def decorator(*args, **kwargs):
        ants = arg_info.annotations

        args_cp = []
        varargs = []

        arg_names = arg_info.args

        if arg_info.varargs != None:
            varargs = _deepcopy(args[len(arg_names):])
            args = args[:len(arg_names)]

        for i, a in enumerate(args):
            arg_name = arg_names[i]
            # only copy value if argument hast read/write annotation
            # do not copy self argument
            if (arg_name in ants and ants[arg_name] == "rw") or arg_name == "self":
                args_cp.append(a)
            else:
                args_cp.append(_deepcopy(a))

        args_cp += varargs

        # arguments which are assigned by name (e.g. x=2)
        kwargs_cp = {}
        for arg_name, value in kwargs.items():
            # only copy value if argument hast read/write annotation
            if arg_name in ants and ants[arg_name] == "rw" or arg_name == "self":
                kwargs_cp[arg_name] = value
            else:
                kwargs_cp[arg_name] = _deepcopy(value)

        return func(*args_cp, **kwargs_cp)
    return decorator


def to_method(instance, func):
    def decorator(*args,**kwargs):
        kwargs["self"]=instance
        return func(*args,**kwargs)
    return decorator
