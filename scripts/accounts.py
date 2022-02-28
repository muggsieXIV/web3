from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/e0ef6687d11f47aeb6cbe5ead7a8755e"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check to see if web3 connection made
print(web3.isConnected())

# Get the node
print(web3.eth.blockNumber)

# Get account's balance
balance = web3.eth.getBalance("0x39C7BC5496f4eaaa1fF75d88E079C22f0519E7b9")

# Print and convernt wei to ether
print(web3.fromWei(balance, "ether"))
