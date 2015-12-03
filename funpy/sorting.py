from funpy.basics import head, tail
from recursive import all


def pairs(xs):
    """Return a sequence of tuples representing all pairs of values in a list."""
    if not xs:
        return []
    return zip(xs, tail(xs))


def sorted(xs):
    """Return True if list is sorted (or an empty list), False otherwise."""
    return all([x <= y for x, y in pairs(xs)])


def qsort(xs):
    """Sort a list using the quick sort algorithm."""
    if not xs:
        return []
    else:
        h = head(xs)
        ts = tail(xs)
        smaller = [n for n in ts if n <= h]
        larger = [n for n in ts if n > h]
        result = qsort(smaller) + [h] + qsort(larger)
        return result
