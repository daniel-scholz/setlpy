from sys import exc_info


def unpack_error(e):
    return e.args[0]