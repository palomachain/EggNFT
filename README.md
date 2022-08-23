# Paloma Egg NFT

## ApeWorx installation

```sh
pipx install eth-ape
ape plugins install infura vyper etherscan
```

## Test

```sh
ape test
```

## Add account

```sh
ape accounts import deployer_account
```

## Deploy on mainnet
Edit Compass-EVM contract address in `scripts/deploy.py`.
```sh
ape run deploy --network :mainnet:infura
```