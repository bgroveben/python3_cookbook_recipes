# In the following sections, we will explore some more advanced pytest
# features.
# To do this, we will need a small project to work with.
# We will be writing a wallet application that enables its users to add or
# spend money in the wallet.
# It will be modeled as a class with two instance methods: spend_cash and
# add_cash.

class InsufficientAmount(Exception):
    pass

class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount("Insufficient Funds")
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount
