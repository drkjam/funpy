# A basic set of recursive functions. See foldable.py for the generalised form using folds.

from basics import head, tail, cons
from boolean import and_, or_

def length(xs):
    if not xs:
        return 0
    else:
        return 1 + length(tail(xs))

def sum(xs):
    if not xs:
        return 0
    else:
        return head(xs) + sum(tail(xs))

def product(xs):
    if not xs:
        return 1
    else:
        return head(xs) * product(tail(xs))

def reverse(xs):
    if not xs:
        return []
    else:
        return reverse(tail(xs)) + [head(xs)]

def map(f, xs):
    if not xs:
        return []
    else:
        return [f(head(xs))] + map(f, tail(xs))

def reduce(f, xs):
    if not xs:
        return 0
    else:
        return f(head(xs), reduce(f, tail(xs)))

def filter(p, xs):
    if not xs:
        return []
    else:
        return [head(xs)] + filter(p, tail(xs)) if p(head(xs)) else filter(p, tail(xs))

def all(xs):
    if not xs:
        return True
    else:
        return and_(head(xs), all(tail(xs)))

def any(xs):
    if not xs:
        return False
    else:
        return or_(head(xs), any(tail(xs)))

__all__ = ['length', 'sum', 'product', 'reverse', 'map', 'reduce', 'filter', 'all', 'any']

