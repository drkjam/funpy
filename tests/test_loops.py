from funpy.loops import fibonacci, factorial


def test_factorial():
    assert map(factorial, range(1, 11)) == [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


def test_fibonacci():
    assert map(fibonacci, range(0, 10)) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
