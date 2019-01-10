import sys


def is_python3():
    return True if sys.version_info.major == 3 else False


def is_python2():
    return True if sys.version_info.major == 2 else False
