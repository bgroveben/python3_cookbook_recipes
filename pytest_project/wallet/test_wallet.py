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
