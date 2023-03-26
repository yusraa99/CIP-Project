import json
import os
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
print('Pathhhh' , print(os.getcwd()))

# Path to the compiled contract JSON file
compiled_contract_path = 'InvestmentEth/build/contracts/Investment.json'
# Deployed contract address (see `migrate` command output: `contract address`)
#deployed_contract_address = '0x8EA3A89D74AE29e75bdfE03f981966D6D3E45212'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract_address = contract_json['networks']
    final_add = contract_address['5777']['address']


# Fetch deployed contract reference
contract = web3.eth.contract(address=final_add, abi=contract_abi)

# Call contract function (this is not persisted to the blockchain)
# message = contract.functions.getData().call()

# user_pro = contract.functions.showAllProdcutUser(1).call()
# print(message)