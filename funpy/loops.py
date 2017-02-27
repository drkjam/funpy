#   Iterative examples of functions usually defined recursively.
#   (Demonstrates the accumulator pattern in a loop without using the stack).


def factorial(n):
    p = 1
    while n > 0:
        n, p = n-1, p*n
    return p


def fibonacci(n):
    x, y = 0, 1
    while n > 0:
        n, x, y = n-1, y, x+y
    return y
