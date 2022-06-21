#!/usr/bin/python3

from conftest import *

def test_mint(EggContract, accounts):
    EggContract.mint(accounts[1], 0, "paloma1hvv77myjavra4rhl0q5qmygu2kn4amgnn6etep", {"from": accounts[0]})
    assert EggContract.balanceOf(accounts[1]) == 1
    print(EggContract.tokenURI(1))