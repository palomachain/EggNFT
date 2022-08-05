#!/usr/bin/python3

import pytest

@pytest.fixture
def EggContract(accounts, project):
    return accounts[0].deploy(project.Egg, accounts[0].address)
