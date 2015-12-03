import pytest

from funpy import recursive, foldable


@pytest.mark.parametrize('module', [recursive, foldable])
def test_length(module):
    assert module.length([]) == 0
    assert module.length([1]) == 1
    assert module.length([1, 2, 3, 4]) == 4


@pytest.mark.parametrize('module', [recursive, foldable])
def test_sum(module):
    assert module.sum([]) == 0
    assert module.sum([1, 2, 3, 4]) == 10


@pytest.mark.parametrize('module', [recursive, foldable])
def test_product(module):
    assert module.product([]) == 1
    assert module.product([1, 2, 3, 4]) == 24


@pytest.mark.parametrize('module', [recursive, foldable])
def test_reverse(module):
    assert module.reverse([]) == []
    assert module.reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


@pytest.mark.parametrize('module', [recursive, foldable])
def test_map(module):
    assert module.map(lambda x: True, []) == []
    assert module.map(lambda x: x + 1, [1, 2, 3, 4]) == [2, 3, 4, 5]


@pytest.mark.parametrize('module', [recursive, foldable])
def test_reduce(module):
    assert module.reduce(lambda x, y: x + y, []) == 0
    assert module.reduce(lambda x, y: x + y, [1, 2, 3, 4]) == 10


@pytest.mark.parametrize('module', [recursive, foldable])
def test_filter(module):
    assert module.filter(lambda x: True, []) == []
    assert module.filter(lambda x: x < 5, [1, 2, 3, 4, 5]) == [1, 2, 3, 4]


@pytest.mark.parametrize('module', [recursive, foldable])
def test_all(module):
    assert module.all([]) == True
    assert module.all([True, True, True]) == True
    assert module.all([True, False, True]) == False

    big_list = [True] * 500
    assert module.all(big_list)

    big_list[-1] = False
    assert module.any(big_list)


@pytest.mark.parametrize('module', [recursive, foldable])
def test_any(module):
    assert module.any([]) == False
    assert module.any([False, False, False]) == False
    assert module.any([True, False, False]) == True

    big_list = [False] * 500
    assert not module.any(big_list)

    big_list[-1] = True
    assert module.any(big_list)
