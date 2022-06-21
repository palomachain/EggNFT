from brownie import accounts, Egg

def main():
    acct = accounts.load("deployer_account")
    Egg.deploy({"from": acct})
