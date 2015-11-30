# Most basic functions, car (head), cdr (tail) and cons.

class EmptyListError(Exception):
    """An empty list was encountered where it was not expected."""

def head(xs):
    if len(xs) < 1:
        raise EmptyListError('empty list')
    return xs[0]

def tail(xs):
    if len(xs) < 1:
        raise EmptyListError('empty list')
    return xs[1:]

def cons(x, xs):
    if hasattr(x, '__iter__'):
        raise Exception('first argument must be scalar!')
    return [x] + xs

__all__ = ['head', 'tail', 'cons']

