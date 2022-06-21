#!/usr/bin/python3

import pytest
from brownie import Egg

@pytest.fixture
def EggContract(accounts):
    return Egg.deploy({"from": accounts[0]})