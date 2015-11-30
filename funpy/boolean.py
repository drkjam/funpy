# Functions that implement boolean operations.
from type_checks import check_type

def and_(x, y):
    check_type(x, bool)
    check_type(y, bool)
    return x and y

def or_(x, y):
    check_type(x, bool)
    check_type(y, bool)
    return x or y

def not_(x):
    check_type(x, bool)
    return not x

__all__ = ['and_', 'or_', 'not_']

