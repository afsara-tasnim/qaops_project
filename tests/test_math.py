import pytest
from utils.math import add, sub


def test_add_simple_sum():
    assert add(2, 2) == 4, "Expected 2+2=4, but function returned another value."


@pytest.mark.parametrize("a,b,expected", [
    (1, 3, 4),
    (10, -2, 8),
    (-5, -5, -10),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected, f"Expected {a}+{b}={expected}"


def test_subtract():
    assert sub(5, 2) == 3