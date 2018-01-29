import pytest

# An example from the docs:
# https://docs.pytest.org/en/latest/

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) != 5

# Let's start with the basics.

def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('The argument must be a string.')
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

# Make sure that the argument type is a string:
def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
