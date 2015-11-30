# Functions for type checking.

def check_type(x, type_):
    if not isinstance(x, type_):
        raise TypeError('expected type %s, not type %s' % (type_, type(x)))

