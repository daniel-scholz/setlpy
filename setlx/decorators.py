from functools import lru_cache as _lru_cache
from inspect import getfullargspec
from copy import deepcopy as _deepcopy


class cached_procedure:
    """ A decorator that caches function results by its input parameters
    
    This is used to mimic the behaviour of of Setlx's cached procedure
    """
    def __init__(self, func):
        self.decorator = _lru_cache(maxsize=None, typed=False)(func)

    def __call__(self, *args, **kwargs):
        return self.decorator(*args, **kwargs)


class to_method:
    """ converts a static method to a method of the given class"""
    def __init__(self, instance, func, static=False):
        self.instance = instance
        self.func = func
        self.static = static

    def __call__(self, *args, **kwargs):
        if self.static:
            kwargs["self"] = self.instance
        else:
            args = (self.instance, *args)
        return self.func(*args, **kwargs)
