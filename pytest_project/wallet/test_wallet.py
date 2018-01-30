# In the following sections, we will explore some more advanced pytest
# features.
# To do this, we will need a small project to work with.

import pytest
from wallet import Wallet, InsufficientAmount

# We will be writing a wallet application that enables its users to add or
# spend money in the wallet.
# It will be modeled as a class with two instance methods: spend_cash and
# add_cash.

def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    asset wallet.balance == 100

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_insufficient_amount_exception():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
