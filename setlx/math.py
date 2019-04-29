""" SetlX's native math functions implemented in python. 

Most of them are just wrappers around functions of the python math package. 
"""

import math


def factorial(num):
    return math.factorial(num)

def acos(value):
    return math.acos(value)


def asin(value):
    return math.asin(value)


def atan(value):
    return math.atan(value)


def cbrt(value):
    return value ** 1/3


def ceil(value):
    return math.ceil(value)


def cos(value):
    return math.cos(value)


def cosh(value):
    return math.cosh(value)


def exp(value):
    return math.exp(value)


def expm1(value):
    return math.expm1(value)


def floor(value):
    return math.floor(value)


def log(value):
    return math.log(value)


def log10(value):
    return math.log10(value)


def log1p(value):
    return math.log1p(value)


def rint(value):
    return float(round(value))


def signum(value):
    return math.copysign(value)


def sin(value):
    return math.sin(value)


def sinh(value):
    return math.sinh(value)


def sqrt(value):
    return math.sqrt(value)


def tan(value):
    return math.tan(value)


def tanh(value):
    return math.tanh(value)


def ulp(value):
    raise NotImplementedError("ulp is not supported")
