from denial import InnerNone, InnerNoneType


def test_inner_none_is_inner_none():
    assert InnerNone is InnerNone  # noqa: PLR0124


def test_inner_none_is_instance_of_inner_none_type():
    assert isinstance(InnerNone, InnerNoneType)


def test_str():
    assert str(InnerNone) == 'InnerNone'


def test_repr():
    assert repr(InnerNone) == 'InnerNone'
