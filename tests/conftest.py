#!/usr/bin/python3

import pytest
from brownie import accounts, Egg, EggMinter

@pytest.fixture
def EggContract(accounts):
    return Egg.deploy({"from": accounts[0]})

@pytest.fixture
def MinterContract(EggContract, userlist):
    print(len(userlist))
    minter = EggMinter.deploy(EggContract, 1, 7, userlist, {"from": accounts[0]})
    EggContract.setMinter(minter, {"from": accounts[0]})
    return minter

@pytest.fixture
def userlist():
    return accounts[0: 10]
