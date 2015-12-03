import pytest

from funpy.basics import head, tail, EmptyListError, cons, null


def test_head():
    assert head([1]) == 1
    assert head([1,2]) == 1

    with pytest.raises(EmptyListError):
        head([])


def test_tail():
    assert tail([1]) == []
    assert tail([1,2]) == [2]
    assert tail([1,2,3]) == [2, 3]

    with pytest.raises(EmptyListError):
        tail([])


def test_cons():
    assert cons(1, []) == [1]
    assert cons(1, cons(2, [])) == [1,2]
    assert cons(1, cons(2, cons(3, []))) == [1,2,3]
    assert cons([], []) == [[]]

    with pytest.raises(TypeError):
        assert cons([], 1)


def test_null():
    assert null([])
    assert not null([1])
    assert not null([1, 2])
    assert not null([1, 2, 3])
