from recursive_factorial import recursive_factorial
import pytest

def test_factorial():
    assert recursive_factorial(5) == 120
    assert recursive_factorial(4) == 24
