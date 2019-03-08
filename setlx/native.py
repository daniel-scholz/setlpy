import sys
import time
import math
import inspect
import multiprocessing
import re
import os
import astor
import random as _random
import itertools
import numbers
import setlx2python.transpiler as transpiler


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
_range = range


def abort(*args):
    raise Exception('abort is not implemented yet')


def abs(value):
    return _abs(value)


def appendFile(*args):
    raise Exception('appendFile is not implemented yet')


def arb(*args):
    raise Exception('arb is not implemented yet')


def args(*args):
    raise Exception('args is not implemented yet')


def ask(*args):
    raise Exception('ask is not implemented yet')


def atan2(*args):
    raise Exception('atan2 is not implemented yet')


def cacheStats(*args):
    raise Exception('cacheStats is not implemented yet')


def canonical(*args):
    raise Exception('canonical is not implemented yet')


def ceil(value):
    return math.ceil(value)


def char(value):
    return chr(value)


def clearCache(*args):
    raise Exception('clearCache is not implemented yet')


def collect(*args):
    raise Exception('collect is not implemented yet')


def compare(*args):
    raise Exception('compare is not implemented yet')


def deleteFile(*args):
    raise Exception('deleteFile is not implemented yet')


def domain(*args):
    raise Exception('domain is not implemented yet')


def double(value):
    return float(value)


def endsWith(*args):
    raise Exception('endsWith is not implemented yet')


def eval(code, global_vars=[], local_vars=[]):
    input = InputStream(code)
    lexer = SetlXgrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SetlXgrammarParser(stream)
    t = transpiler.Transpiler(parser.expr(False).ex)
    py_code = astor.to_source(t.to_python(t.root))
    return _eval(py_code, global_vars, local_vars)


def evalTerm(*args):
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
    raise Exception('fct is not implemented yet')


def first(iterable):
    return iterable[0]


def floor(value):
    return math.floor(value)

# This is the setlx from function. renamed because "from" is a python keword


def v_from(*args):
    raise Exception('v_from is not implemented yet')


def fromB(*args):
    raise Exception('fromB is not implemented yet')


def fromE(*args):
    raise Exception('fromE is not implemented yet')


def get(*args):
    raise Exception('get is not implemented yet')


def getOsID(*args):
    raise Exception('getOsID is not implemented yet')


def getScope(*args):
    raise Exception('getScope is not implemented yet')


def getTerm(*args):
    raise Exception('getTerm is not implemented yet')


def hypot(*args):
    raise Exception('hypot is not implemented yet')


def int(value):
    return _int(value)


def isBoolean(value):
    return isinstance(value, bool)


def isClass(value):
    return inspect.isclass(value)


def isDouble(value):
    return isinstance(value, float)


def isError(*args):
    raise Exception('isError is not implemented yet')


def isInfinite(value):
    return value == math.inf


def isInteger(value):
    return isinstance(value, _int)


def isList(value):
    return isinstance(value, list)


def isMap(*args):
    raise Exception('isMap is not implemented yet')


def isNumber(n):
    # bool is int in python (True=0, False=1)
    return isinstance(n, numbers.Number) and not isinstance(n, bool)


def isObject(obj):
    return inspect.isclass(obj)


def isPrime(n):
    if not isinstance(n, int):
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


def isProbablePrime(*args):
    raise Exception('isProbablePrime is not implemented yet')


def isProcedure(*args):
    raise Exception('isProcedure is not implemented yet')


def isRational(*args):
    raise Exception('isRational is not implemented yet')


def isSet(*args):
    raise Exception('isSet is not implemented yet')


def isString(value):
    return isinstance(value, _str)


def isTerm(*args):
    raise Exception('isTerm is not supported')


def isVariable(*args):
    raise Exception('isVariable is not implemented yet')


def join(*args):
    raise Exception('join is not implemented yet')


def la_cond(*args):
    raise Exception('la_cond is not implemented yet')


def la_det(*args):
    raise Exception('la_det is not implemented yet')


def la_eigenValues(*args):
    raise Exception('la_eigenValues is not implemented yet')


def la_eigenVectors(*args):
    raise Exception('la_eigenVectors is not implemented yet')


def la_hadamard(*args):
    raise Exception('la_hadamard is not implemented yet')


def la_isMatrix(*args):
    raise Exception('la_isMatrix is not implemented yet')


def la_isVector(*args):
    raise Exception('la_isVector is not implemented yet')


def la_matrix(*args):
    raise Exception('la_matrix is not implemented yet')


def la_pseudoInverse(*args):
    raise Exception('la_pseudoInverse is not implemented yet')


def la_solve(*args):
    raise Exception('la_solve is not implemented yet')


def la_svd(*args):
    raise Exception('la_svd is not implemented yet')


def la_vector(*args):
    raise Exception('la_vector is not implemented yet')


def last(*args):
    raise Exception('last is not implemented yet')


def load(file, source_file=""):
    source = os.path.dirname(os.path.realpath(source_file))
    path = os.path.join(source, file)
    path = os.path.splitext(path)[0]+".py"
    with open(path) as f:
        exec(f.read())


def loadLibrary(*args):
    raise Exception('loadLibrary is not implemented yet')


def logo(*args):
    raise Exception('logo is not implemented yet')


def makeTerm(*args):
    raise Exception('makeTerm is not implemented yet')


def matches(*args):
    raise Exception('matches is not implemented yet')


def mathConst(name):
    # TODO throw error on unknown name
    return {"pi": math.pi, "e": math.e, "infinity": math.inf}[name]


def max(collection):
    return _max(collection)


def min(collection):
    return _min(collection)


def multiLineMode(*args):
    raise Exception('multiLineMode is not implemented yet')


def nCPUs(*args):
    return multiprocessing.cpu_count()


def nDecimalPlaces(number, places):
    return ('{0:.'+str(places)+'f}').format(number)


def nPrint(*args):
    return _print(*args, end="")


def nPrintErr(*args):
    _print(*args, sep=" ", end="", file=sys.stderr)


def nextPermutation(*args):
    raise Exception('nextPermutation is not implemented yet')


def nextProbablePrime(*args):
    raise Exception('nextProbablePrime is not implemented yet')


def now():
    return int(round(time.time() * 1000))


def parse(*args):
    raise Exception('parse is not implemented yet')


def parseStatements(*args):
    raise Exception('parseStatements is not implemented yet')


def permutations(iterable):
    # TODO for sets
    return list(itertools.permutations(iterable))


def pow(*args):
    raise Exception('pow is not implemented yet')


def print(*args):
    _print(*args, sep=" ")


def printErr(*args):
    _print(*args, sep=" ", file=sys.stderr)


def random(n=1.0):
    return _random.random()*n


def range(*args):
    raise Exception('range is not implemented yet')


def rational(*args):
    raise Exception('rational is not implemented yet')


def read(*args):
    raise Exception('read is not implemented yet')


def readFile(file):
    f = open(file)
    content = f.readlines()
    f.close()
    return content


def replace(*args):
    raise Exception('replace is not implemented yet')


def replaceFirst(*args):
    raise Exception('replaceFirst is not implemented yet')


def resetRandom():
    _random.seed(0)


def reverse(*args):
    raise Exception('reverse is not implemented yet')


def rnd(iterable):
    rnd_index = _random.randint(0, len(iterable)-1)
    return iterable[rnd_index]


def round(*args):
    raise Exception('round is not implemented yet')


def run(*args):
    raise Exception('run is not implemented yet')


def shuffle(*args):
    raise Exception('shuffle is not implemented yet')


def sleep(milliseconds):
    time.sleep(milliseconds*1000)


def sort(*args):
    raise Exception('sort is not implemented yet')


def split(string, pattern):
    return re.compile(pattern).split(string)


def sqrt(n):
    return math.sqrt(n)


def startsWith(*args):
    raise Exception('startsWith is not implemented yet')


def stop(*args):
    raise Exception('stop is not implemented yet')


def str(arg):
    return _str(arg)


def throw(e):
    raise Exception(e)


def toLowerCase(*args):
    raise Exception('toLowerCase is not implemented yet')


def toUpperCase(*args):
    raise Exception('toUpperCase is not implemented yet')


def trace(*args):
    raise Exception('trace is not implemented yet')


def trim(*args):
    raise Exception('trim is not implemented yet')


def writeExamples(*args):
    raise Exception('writeExamples is not implemented yet')


def writeFile(*args):
    raise Exception('writeFile is not implemented yet')


def writeLibrary(*args):
    raise Exception('writeLibrary is not implemented yet')
