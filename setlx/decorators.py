from functools import lru_cache as _lru_cache
from inspect import getfullargspec
from copy import deepcopy as _deepcopy


class cached_procedure:
    def __init__(self, func):
        self.decorator = _lru_cache(maxsize=None, typed=False)(func)
    
    def __call__(self, *args, **kwargs):
        return self.decorator(*args,**kwargs)

def to_method(instance, func):
    def decorator(*args,**kwargs):
        kwargs["self"]=instance
        return func(*args,**kwargs)
    return decorator
