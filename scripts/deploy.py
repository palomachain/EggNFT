from ape import accounts, project

def main():
    acct = accounts.load("deployer_account")
    COMPASS_EVM = "0x0000000000000000000000000000000000000000"
    contract = acct.deploy(project.Egg, COMPASS_EVM)
    return contract