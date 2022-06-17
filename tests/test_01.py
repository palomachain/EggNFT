#!/usr/bin/python3

import pytest, brownie

from conftest import *

def test_mint(EggContract, MinterContract, accounts):
    for i in range(7):
        MinterContract.mint({"from": accounts[0]})
        for account in accounts:
            print(EggContract.balanceOf(account))
            print("------------")