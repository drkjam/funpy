# Functions defined in terms of the 'fold*' higher order functions.

from basics import head, tail
from boolean import and_, or_


def foldr(f, v, xs):
    if not xs:
        return v
    else:
        return f(head(xs), foldr(f, v, tail(xs)))


def length(xs):
    return foldr(lambda _, ys: 1 + ys, 0, xs)


def sum(xs):
    return foldr(lambda x, ys: x + ys, 0, xs)


def product(xs):
    return foldr(lambda x, ys: x * ys, 1, xs)


def reverse(xs):
    return foldr(lambda x, ys: ys + [x], [], xs)


def map(f, xs):
    return foldr(lambda x, ys: [f(x)] + ys, [], xs)


def reduce(f, xs):
    return foldr(lambda x, ys: f(x, ys), 0, xs)


def filter(p, xs):
    return foldr(lambda x, ys: [x] + ys if p(x) else ys, [], xs)


def all(xs):
    return foldr(lambda x, ys: and_(x, ys), True, xs)


def any(xs):
    return foldr(lambda x, ys: or_(x, ys), False, xs)


__all__ = ['foldr', 'length', 'sum', 'product', 'reverse', 'map', 'reduce', 'filter', 'all', 'any']
