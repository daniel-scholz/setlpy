"""
module for predefined setlX functions
"""

import sys
import time
import math
import inspect
import multiprocessing
import re
import os
import astor
import random as _random
import typing
import itertools
import platform
import setlx2python.transpiler as transpiler
from copy import deepcopy
from collections import Counter

from .vector import Vector
from .matrix import Matrix
from .utils import is_number, is_integer
from .splayset import Set
from .errors import UserException

from setlx2python.grammar.SetlXgrammarParser import SetlXgrammarParser
from setlx2python.grammar.SetlXgrammarLexer import SetlXgrammarLexer
from setlx2python.grammar.SetlXgrammarListener import SetlXgrammarListener
from antlr4 import InputStream, CommonTokenStream


_print = print
_str = str
_abs = abs
_int = int
_max = max
_min = min
_eval = eval
_pow = pow
_range = range
_round = round


def abort(msg):
    raise Exception(msg)


def abs(value):
    return _abs(value)


def appendFile(*args):
    raise NotImplementedError('appendFile is not implemented yet')


def arb(value):
    if isinstance(value, (list, tuple, _str)):
        size = len(value)
        v = value[0 if size % 2 == 0 else -1]
        return v
    try:
        return value.__arb__()
    except:
        raise Exception(f"Argument '{value}' is not a collection value.")


def args(term):
    raise Exception('args is not supported')


def ask(*args):
    raise NotImplementedError('ask is not implemented yet')


def atan2(y, x):
    return math.atan2(y, x)


def cacheStats(fn):
    # TODO wrap in setlx structures
    return fn.cache.cache_info()


def canonical(term):
    raise Exception('canonical is not supported')


def ceil(value):
    return math.ceil(value)


def char(value):
    return chr(value)


def clearCache(cached_procedure):
    raise NotImplementedError('clearCache is not implemented yet')


def collect(list):
    dic = Counter(list)
    return Set([[key, dic[key]] for key in dic])


def compare(*args):
    raise NotImplementedError('compare is not implemented yet')


def deleteFile(path):
    try:
        os.remove(path)
        return True
    except:
        return False


def domain(set):
    return set.__domain__()


def double(value):
    return float(value)


def endsWith(string, suffix):
    return string.endswith(suffix)


def eval(code, global_vars={}, local_vars={}):
    input = InputStream(code)
    lexer = SetlXgrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SetlXgrammarParser(stream)
    t = transpiler.Transpiler(parser.expr(False).ex)
    py_code = astor.to_source(t.to_python(t.root))
    return _eval(py_code, global_vars, local_vars)


def evalTerm(term):
    raise Exception('evalTerm is not supported')


def execute(code, global_vars=[], local_vars=[]):
    input = InputStream(code)
    lexer = SetlXgrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SetlXgrammarParser(stream)
    t = transpiler.Transpiler(parser.block().blk)
    py_code = astor.to_source(t.transpile())
    return exec(py_code, global_vars, local_vars)


def fct(*args):
    raise NotImplementedError('fct is not implemented yet')


def first(value):
    if isinstance(value, (list, _str)):
        return value[0]
    try:
        return value.first()
    except:
        raise Exception(
            f"Can not get last member from operand; '{value}' is not a collection value.")


def floor(value):
    return math.floor(value)

# This is the setlx from function. renamed because "from" is a python keword


def v_from(value):
    if isinstance(value, (list, _str)):
        size = len(value)
        index = 0 if size % 2 == 0 else -1
        v = value[index]
        del value[index]
        return v
    try:
        return value.__from__()
    except:
        raise Exception(f"Argument '{value}' is not a collection value.")


def fromB(value):
    if isinstance(value, (list, _str)):
        v = value[0]
        del value[0]
        return v
    try:
        return value.__fromB__()
    except NotImplementedError:
        raise Exception(f"Argument '{value}' is not a collection value.")


def fromE(value):
    if isinstance(value, (list, _str)):
        v = value[-1]
        del value[-1]
        return v
    try:
        return value.__fromE__()
    except:
        raise Exception(f"Argument '{value}' is not a collection value.")


def get(*args):
    raise NotImplementedError('get is not implemented yet')


def getOsID():
    return f"{platform.system()} {platform.release()}"


def getScope(term):
    raise Exception('getScope is not supported')


def getTerm(term):
    raise Exception('getTerm is not supported')


def hypot(x, y):
    return sqrt(x**2+y**2)


def int(value):
    return _int(value)


def isBoolean(value):
    return isinstance(value, bool)


def isClass(value):
    return inspect.isclass(value)


def isDouble(value):
    return isinstance(value, float)


def isError(value):
    return isinstance(value, Exception)


def isInfinite(value):
    return value == math.inf


def isInteger(value):
    return is_integer(value)


def isList(value):
    return isinstance(value, list)


def isMap(*args):
    """
    checks if list of arguments is a map(aka dict in Python)
    """
    for a in args:
        if not isinstance(a, dict):
            return False
    return True


def isNumber(n):
    return is_number(n)


def isObject(obj):
    return inspect.isclass(obj)


def isPrime(n):
    if not isInteger(n):
        return False
    else:
        # Sieve of Eratosthenes.
        # see https://stackoverflow.com/a/17377939
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False

        sqr = int(math.sqrt(n)) + 1

        for divisor in _range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True


def isProbablePrime(n, k=15):
    """
    based on https://gist.github.com/Ayrx/5884790
    """
    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in _range(k):
        a = _random.randrange(2, n - 1)
        x = _pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in _range(r - 1):
            x = _pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def isProcedure(value):
    return hasattr(value, '__call__')


def isRational(n):
    return not isinstance(n, complex)


def isSet(value):
    return isinstance(value, Set)


def isString(value):
    return isinstance(value, _str)


def isTerm(*args):
    raise Exception('isTerm is not supported')


def isVariable(*args):
    raise NotImplementedError('isVariable is not implemented yet')


def join(collection, seperator):
    return seperator.join([str(c) for c in collection])


def la_cond(matrix):
    return matrix.__cond__()  # TODO


def la_det(matrix):
    return matrix.__det__()  # TODO


def la_eigenValues(*args):
    raise NotImplementedError('la_eigenValues is not implemented yet')


def la_eigenVectors(*args):
    raise NotImplementedError('la_eigenVectors is not implemented yet')


def la_hadamard(*args):
    raise NotImplementedError('la_hadamard is not implemented yet')


def la_isMatrix(value):
    return isinstance(value, Matrix)


def la_isVector(value):
    return isinstance(value, Vector)


def la_matrix(value):
    if isinstance(value, list):
        return Matrix(value)
    elif isinstance(value, Vector):
        return Matrix([x for x in value.to_list()])
    raise Exception(
        "Matrices can only be created from collections or vectors.")


def la_pseudoInverse(*args):
    raise NotImplementedError('la_pseudoInverse is not implemented yet')


def la_solve(*args):
    raise NotImplementedError('la_solve is not implemented yet')


def la_svd(*args):
    raise NotImplementedError('la_svd is not implemented yet')


def la_vector(value):
    if isinstance(value, list):
        return Vector(value)
    elif isinstance(value, Matrix):
        return value.to_vector()
    raise Exception(
        "Vectors can only be created from collections or matrices.")


def last(value):
    if isinstance(value, (list, _str)):
        return value[-1]
    try:
        return value.last()
    except:
        raise Exception(
            f"Can not get last member from operand; '{value}' is not a collection value.")


def load(file, source_file=""):
    source = os.path.dirname(os.path.realpath(source_file))
    path = os.path.join(source, file)
    path = os.path.splitext(path)[0]+".py"
    with open(path) as f:
        exec(f.read())


def loadLibrary(*args):
    raise NotImplementedError('loadLibrary is not implemented yet')


def logo(*args):
    raise Exception('logo is not supported')


def makeTerm(*args):
    raise Exception('makeTerm is not supported')


def matches(string, pattern, captureGroups=False):
    match = re.match(pattern, string)
    if captureGroups:
        raise Exception('captureGroups is not supported')
    return match != None


def mathConst(name):
    try:
        return {"pi": math.pi, "e": math.e, "infinity": math.inf}[name.lower()]
    except:
        raise Exception(
            f"Name-argument {name} is not a known constant or not a string.")


def max(collection):
    return _max(collection)


def min(collection):
    return _min(collection)


def multiLineMode(*args):
    raise Exception('multiLineMode is not supported')


def nCPUs(*args):
    return multiprocessing.cpu_count()


def nDecimalPlaces(number, places):
    return ('{0:.'+str(places)+'f}').format(number)


def nPrint(*args):
    return _print(*args, end="")


def nPrintErr(*args):
    _print(*args, sep=" ", end="", file=sys.stderr)


def nextPermutation(list):
    if len(list) < 2:
        return None

    p = list[::]

    a = len(p) - 2
    while a >= 0 and p[a] >= p[a + 1]:
        a -= 1

    if a == -1:
        return None

    b = len(p) - 1
    while p[b] <= p[a]:
        b -= 1

    tmp = p[a]
    p[a] = p[b]
    p[b] = tmp

    i = a + 1
    j = len(p) - 1
    while i < j:
        tmp = p[i]
        p[i] = p[j]
        p[j] = tmp
        i += 1
        j += 1

    return p


def nextProbablePrime(*args):
    raise NotImplementedError('nextProbablePrime is not implemented yet')


def now():
    return int(_round(time.time() * 1000))


def parse(*args):
    raise Exception('parse is not supported')


def parseStatements(*args):
    raise Exception('parseStatements is not supported')


def permutations(iterable):
    # TODO for sets
    return list(itertools.permutations(iterable))


def pow(s):
    raise NotImplementedError("power set is not yet implemented")


def print(*args):
    _print(*args, sep="")


def printErr(*args):
    _print(*args, sep="", file=sys.stderr)


def random(n=1.0):
    return _random.random()*n


def range(map):  # map is set
    return map.__range__()


def rational(*args):
    raise NotImplementedError('rational is not implemented yet')


def read(text):
    return input(text)


def readFile(file):
    f = open(file)
    content = f.readlines()
    f.close()
    return content


def replace(string, pattern, replacement):
    return re.sub(pattern, replacement, string)


def replaceFirst(string, pattern, replacement):
    return re.subn(pattern, replacement, string, 1)


def resetRandom():
    _random.seed(0)


def reverse(value):
    if isinstance(value, (list, str)):
        return value[::-1]
    raise Exception(f"Operand '{value}' is not a list or string.")


def rnd(numberOrCollection, numberOfChoices=None):
    if isinstance(numberOrCollection, Set):
        return numberOrCollection.__rnd__()
    if isinstance(numberOrCollection, _int):
        return _random.randint(0, numberOrCollection)
    if numberOfChoices != None:
        raise NotImplementedError("numberOfChoices is not implemented yet")
    if len(numberOrCollection) == 0:
        return None
    rnd_index = _random.randint(1, len(numberOrCollection))
    return numberOrCollection[rnd_index]


def round(n):
    return _round(n)


def run(*args):
    raise NotImplementedError('run is not implemented yet')


def shuffle(collection):
    if isinstance(collection, list):
        cp = deepcopy(collection)
        _random.shuffle(cp)
        return cp
    if isinstance(collection, _str):
        cp = list(collection)
        _random.shuffle(cp)
        return "".join(cp)
    raise Exception(f"Cannot shuffle type {type(collection)}")


def sleep(milliseconds):
    time.sleep(milliseconds*1000)


def sort(collection):
    if isinstance(collection, list):
        cp = deepcopy(collection)
        cp.sort()
        return cp
    if isinstance(collection, _str):
        cp = list(collection)
        cp.sort()
        return "".join(cp)
    raise Exception(f"Cannot sort type {type(collection)}")


def split(string, pattern):
    return re.compile(pattern).split(string)


def sqrt(n):
    return math.sqrt(n)


def startsWith(string, prefix):
    return string.startswith(prefix)


def stop(*args):
    raise Exception('stop is not supported')


def str(arg):
    return _str(arg)


def throw(e):
    raise UserException(e)


def toLowerCase(string):
    return string.lower()


def toUpperCase(string):
    return string.upper()


def trace(*args):
    raise NotImplementedError('trace is not implemented yet')


def trim(string):
    return string.strip()


def writeExamples(*args):
    raise Exception('writeExamples is not supported')


def writeFile(path, lines):
    with open(path, "w") as f:
        f.write("\n".join(lines))


def writeLibrary(*args):
    raise Exception('writeLibrary is not supported')
