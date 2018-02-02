# In the following sections, we will explore some more advanced pytest
# features.
# To do this, we will need a small project to work with.

import pytest
from wallet import Wallet, InsufficientAmount

# We will be writing a wallet application that enables its users to add or
# spend money in the wallet.
# It will be modeled as a class with two instance methods: spend_cash and
# add_cash.

# Refactor our previous tests to use test fixtures where appropriate.
# It is a good practice to add docstrings for your fixtures.
# To see all the available fixtures, run the following command:
# [=> pytest --fixtures

@pytest.fixture
def empty_wallet():
    """
    Returns a Wallet instance with a zero balance.
    """
    return Wallet()

@pytest.fixture
def wallet():
    """
    Returns a Wallet instance with a balance of 20.
    """
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_insufficient_amount_exception(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)


# Having tested the individual methods in the Wallet class, the next step we
# should take is to test various combinations of these methods.
# This is to answer questions such as "If I have an initial balance of 30, and
# spend 20, then add 100, and later on spend 50, how much should the balance
# be?"
# As you can imagine, writing out those steps in the tests would be tedious,
# and pytest provides quite a delightful solution: Parametrized test functions.
# To capture a scenario like the one above, we can write a test:

"""
This enables us to test different scenarios, all in one function.
We make use of the @pytest.mark.parametrize decorator, where we can specify the
names of the arguments that will be passed to the test function, and a list of
arguments corresponding to the names.
"""
@pytest.mark.parametrize("earned, spent, expected", [
    (30, 10, 20),
    (20, 2, 18),
])

def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected

# To make our tests less repetitive, we can go further and combine test
# fixtures and parametrize test functions.
# To demonstrate this, let's replace the wallet initialization code with a test # fixture as we did before.

@pytest.fixture
def my_wallet():
    """
    Returns a Wallet instance witha zero balance.
    """
    return Wallet()

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])

def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
