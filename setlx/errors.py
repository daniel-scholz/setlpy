from sys import exc_info


def unpack_error(e):
    return e.args[0]

# All exceptions thrown in code
class UserException(Exception):pass

# Exception thrown by backtrack statement
class BacktrackException(Exception): pass