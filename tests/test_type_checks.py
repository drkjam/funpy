import pytest

from funpy.type_checks import check_type


def test_type_checks():
    check_type(True, bool) is None

    with pytest.raises(TypeError):
        check_type(1, bool) is None
