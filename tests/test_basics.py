import pytest

from funpy.basics import head, tail, EmptyListError


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
