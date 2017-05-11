# test_wallet_fixture_improved.py

import pytest
from wallet import Wallet

# Improved test_wallet_fixture, combining test fixtures and parametrize test functions.
# I have replace the wallet initialization code with a test fixture


# This feature is the same as empty_wallet fixture. It returns a wallet instance with a balance of 0.
@pytest.fixture
def my_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

# To use both the fixture and the parametrized functions in the test,
# we include the fixture as the first argument, and the parameters as the rest of the arguments
@pytest.mark.parametrize("earned, spent, expected", [
    (80, 10, 60),
    (3000, 3000, 0),
])
def test_transaction(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
