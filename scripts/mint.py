from brownie import accounts, Egg

def main():
    acct = accounts.load("deployer_account")
    Egg.mint("0x6513cb2f5E59c768a28958FBBDa6e06B9B29B8Eb", "paloma1a8m2ldry3psf77nza50ss5dwn9jm8qr82vtja4", 1, {"from": acct})