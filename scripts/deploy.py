from ape import accounts, project

def main():
    acct = accounts.load("deployer_account")
    COMPASS_EVM = "0x24B10a62385C2d04F3f04Dd55297ADD7b4502530"
    START_ID = 46
    contract = acct.deploy(project.Egg, COMPASS_EVM, START_ID, max_priority_fee="1 wei", max_fee="50 gwei")
    return contract