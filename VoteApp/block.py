import datetime
import json

from web3 import Web3, HTTPProvider
# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = r"E:\e_voting\node_modules\.bin\build\contracts\Structreq.json"
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x7194B83b6D13743547bD2523766CbABf1ab894d1'

print("started")
#--------------------


data=input().split("-")
print(data,"=================")
try:
    with open(
            r'E:\e_voting\node_modules\.bin\build\contracts\Structreq.json') as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address='0x7194B83b6D13743547bD2523766CbABf1ab894d1', abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    message2 = contract.functions.addreq(blocknumber + 1, str(data[0]), str(data[1]),
                                         str(datetime.datetime.now().strftime("%Y-%m-%d")),
                                         ).transact({"from": web3.eth.accounts[0]})
    
except Exception as r:
    print(r)