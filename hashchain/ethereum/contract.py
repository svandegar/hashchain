from web3 import Web3, HTTPProvider
import json

CONTRACT_JSON_PATH = 'hashchain/ethereum/Hashchain.json'


class EthContract():
    def __init__(self):
        with open(CONTRACT_JSON_PATH) as file:
            self.contract_dict = json.load(file)

    def deploy(self,
               sender_public_key: str,
               sender_private_key: str,
               provider_url: str):
        self.owner = Web3.toChecksumAddress(sender_public_key)
        self._owner_private_key = sender_private_key
        self._provider_address = provider_url
        self.w3 = Web3(HTTPProvider(self._provider_address))
        self.abi = self.contract_dict['abi']
        self.contract = self.w3.eth.contract(bytecode=self.contract_dict['bytecode'],
                                             abi=self.contract_dict['abi'])

        txn_dict = dict(
            nonce=self.w3.eth.getTransactionCount(self.owner),
            gasPrice=self.w3.eth.gasPrice,
            gas=2000000)

        txn = self.contract.constructor().buildTransaction(txn_dict)
        signed_txn = self.w3.eth.account.signTransaction(txn, self._owner_private_key)

        self.txn_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        return self.txn_hash

    def get_txn_receipt(self):
        txn_receipt = self.w3.eth.getTransactionReceipt(self.txn_hash)

        self.address = txn_receipt['contractAddress']

        return txn_receipt
