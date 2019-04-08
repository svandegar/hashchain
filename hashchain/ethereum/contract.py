from web3 import Web3, HTTPProvider
import json

CONTRACT_JSON_PATH = 'hashchain/ethereum/Hashchain.json'


class EthContract():
    """
    Solidity contract encapsulated in a Python object
    """
    def __init__(self):
        """
        Get the contract definition from the JSON file located at 'hashchain/ethereum/Hashchain.json'
        """
        with open(CONTRACT_JSON_PATH) as file:
            self.contract_dict = json.load(file)

    def deploy(self,
               sender_public_key: str,
               sender_private_key: str,
               provider_url: str) -> str:
        """
        Deploy the Solidoty Smart contract to the Ethereum blockchain
        :param sender_public_key: public key of the sender
        :param sender_private_key: private key of the sender
        :param provider_url: address of the Ethereum connection provider
        :return: str: transaction hash
        """
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

    def get_txn_receipt(self) -> dict:
        """
        Add the address variable to EthContract and returns the transaction receipt of the contract creation transaction.
         If the transaction has not yet been mined returns None
        :return: dict: transaction receipt or None
        """
        txn_receipt = self.w3.eth.getTransactionReceipt(self.txn_hash)

        if txn_receipt:
            self.address = txn_receipt['contractAddress']

        return txn_receipt
