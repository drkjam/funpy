from funpy.boolean import and_, or_, not_


def test_and_():
    assert and_(True, True) == True
    assert and_(True, False) == False
    assert and_(False, True) == False
    assert and_(False, False) == False


def test_or_():
    assert or_(True, True) == True
    assert or_(True, False) == True
    assert or_(False, True) == True
    assert or_(False, False) == False


def test_not_():
    assert not_(True) == False
    assert not_(False) == True
