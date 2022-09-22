#!/usr/bin/python3

from conftest import *

def test_mint(EggContract, accounts):
    EggContract.mint(accounts[1], 0, "paloma1hvv77myjavra4rhl0q5qmygu2kn4amgnn6etep", sender=accounts[0])
    assert EggContract.balanceOf(accounts[1].address) == 1
    EggContract.transferFrom(accounts[1].address, accounts[0].address, 0, sender=accounts[1])
    EggContract.balanceOf(accounts[0].address) == 1