# @version 0.3.3

WHITELIST_LENGTH: constant(uint256) = 10
BASE_TOKEN_ID: immutable(uint256)
MINT_COUNT: immutable(uint256)
BASE_TIMESTAMP: immutable(uint256)
EGG: immutable(address)
count: public(uint256)
whitelist: public(address[WHITELIST_LENGTH])
minted: HashMap[address, bool]
epoch: uint256

interface ERC721:
    def mint(_to: address, _tokenId: uint256) -> bool: nonpayable

@external
def __init__(egg: address, base_token_id: uint256, mint_count: uint256, _whitelist: address[WHITELIST_LENGTH]):
    EGG = egg
    MINT_COUNT = mint_count
    BASE_TOKEN_ID = base_token_id
    BASE_TIMESTAMP = block.timestamp % 86400
    self.whitelist = _whitelist

@external
@pure
def egg() -> address:
    return EGG

@internal
@view
def pseudo_rand(seed: uint256, length: uint256) -> uint256:
    return convert(keccak256(concat(
        convert(seed, bytes32),
        convert(block.coinbase, bytes20),
        convert(block.difficulty, bytes32),
        convert(block.timestamp, bytes32),
        convert(tx.gasprice, bytes32)
    )), uint256) % length

@external
def mint():
    assert (block.timestamp - BASE_TIMESTAMP) / 86400 > self.epoch
    winner_id: uint256 = 0
    _count: uint256 = self.count
    assert _count < MINT_COUNT, "overmint"
    for seed in range(100000):
        winner_id = self.pseudo_rand(seed, WHITELIST_LENGTH)
        winner: address = self.whitelist[winner_id]
        if self.minted[winner] == False:
            ERC721(EGG).mint(self.whitelist[winner_id], _count + BASE_TOKEN_ID)
            self.count = _count + 1
            self.epoch = (block.timestamp - BASE_TIMESTAMP) / 86400
            self.minted[winner] = True
            break
