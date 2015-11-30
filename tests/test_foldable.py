from funpy.foldable import *

def test_length():
    assert length([]) == 0
    assert length([1]) == 1
    assert length([1,2,3,4]) == 4

def test_sum():
    assert sum([]) == 0
    assert sum([1, 2, 3, 4]) == 10

def test_product():
    assert product([]) == 1
    assert product([1, 2, 3, 4]) == 24

def test_reverse():
    assert reverse([]) == []
    assert reverse([1,2,3,4,5]) == [5, 4, 3, 2, 1]

def test_map():
    assert map(lambda x: True, []) == []
    assert map(lambda x: x + 1, [1, 2, 3, 4]) == [2, 3, 4, 5]

def test_reduce():
    assert reduce(lambda x, y: x + y, []) == 0
    assert reduce(lambda x, y: x + y, [1, 2, 3, 4]) == 10

def filter():
    assert filter(lambda x: True, []) == []
    assert filter(lambda x: x < 5, [1, 2, 3, 4, 5]) == [1, 2, 3, 4]

def all(xs):
    assert all([]) == True
    assert all([True, True, True]) == True
    assert all([True, False, True]) == False

def any(xs):
    assert any([]) == False
    assert any([False, False, False]) == False
    assert all([True, False, False]) == True

