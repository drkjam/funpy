import random
from funpy.sorting import pairs, sorted, qsort


def test_pairs():
    assert pairs([]) == []
    assert pairs([1]) == []
    assert pairs([1,2]) == [(1, 2)]
    assert pairs([1,2,3]) == [(1, 2), (2, 3)]
    assert pairs([1,2,3,4]) == [(1, 2), (2, 3), (3, 4)]


def test_sorted():
    assert sorted([])
    assert sorted([1])
    assert sorted([1, 2])
    assert sorted([1, 2, 3])
    assert not sorted([2, 1])
    assert not sorted([3, 2, 1])
    assert not sorted([3, 1, 2])


def test_qsort():
    l1 = range(50)
    assert sorted(l1)
    l2 = l1[:]
    random.shuffle(l2)
    assert not sorted(l2)
    l3 = qsort(l2)
    assert sorted(l3)
    assert l3 == l1
