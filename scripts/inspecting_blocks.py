from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/e0ef6687d11f47aeb6cbe5ead7a8755e"
web3 = Web3(Web3.HTTPProvider(infura_url))

# get latest block number
print(web3.eth.blockNumber)

# get latest block
print(web3.eth.getBlock('latest'))

# get latest 10 blocks
latest = web3.eth.blockNumber
for i in range(0, 10):
    print(web3.eth.getBlock(latest - i))

# get transaction from specific block
hash = '0x39C7BC5496f4eaaa1fF75d88E079C22f0519E7b9'
print(web3.eth.getTransactionByBlock(hash, 2))
