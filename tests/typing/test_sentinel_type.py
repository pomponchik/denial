import pytest

from denial import InnerNone, InnerNoneType, Sentinel


@pytest.mark.mypy_testing
def test_sentinel_is_including_inner_none_and_just_none():
    variable: Sentinel = InnerNone  # noqa: F841
    another_variable: Sentinel = None  # noqa: F841


@pytest.mark.mypy_testing
def test_sentinel_is_including_inner_none_type():
    variable: Sentinel = InnerNoneType()  # noqa: F841
    another_variable: Sentinel = InnerNoneType(123)  # noqa: F841
    another_else_variable: Sentinel = InnerNoneType('kek')  # noqa: F841


@pytest.mark.mypy_testing
def test_wrong_using_of_sentinel():
    variable: Sentinel = 123 # E: [assignment] # noqa: F841
    another_variable: Sentinel = 'kek' # E: [assignment] # noqa: F841
    another_else_variable: Sentinel = False # E: [assignment] # noqa: F841
