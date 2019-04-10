from web3 import Web3, HTTPProvider
import hashlib


class EthConnector():
    """
    Connector to interact with a smart contract on the Ethereum blockchain.
    """
    def __init__(self,
                 contract_abi: str,
                 contract_address: str,
                 sender_public_key: str,
                 sender_private_key: str,
                 provider_url: str):
        """

        :param contract_abi: smart contract's abi JSON string
        :param contract_address: smart contract address
        :param sender_public_key: public key of the sender
        :param sender_private_key: private key of the sender
        :param provider_url: address of the Ethereum connection provider
        """
        self._contract_abi = contract_abi
        self._contract_address = Web3.toChecksumAddress(contract_address)
        self._sender_public_key = Web3.toChecksumAddress(sender_public_key)
        self._sender_private_key = sender_private_key
        self._provider_address = provider_url
        self.w3 = Web3(HTTPProvider(self._provider_address))
        self.contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)

    def record(self, key: str, hash: str, wait = False):
        """
        Records the key and hash in the smart contract storage
        :param key: indexed key, used to retrieve the hash
        :param hash: hash of the record
        :param wait: wait for the transaction to receipt before completing
        :return: transaction hash
        """
        key_hash = hashlib.sha3_256(key.encode('utf-8'))
        hash_bytes = bytes.fromhex(hash)
        txn_dict = dict(
            nonce=self.w3.eth.getTransactionCount(self._sender_public_key),
            gasPrice=self.w3.eth.gasPrice,
            gas=2000000
        )

        txn = self.contract.functions.record(key_hash.digest(), hash_bytes).buildTransaction(txn_dict)
        signed_txn = self.w3.eth.account.signTransaction(txn, self._sender_private_key)
        txn_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        if wait:
            self.w3.eth.waitForTransactionReceipt(txn_hash)
            return txn_hash
        else:
            return txn_hash

    def get_record(self, key: str):
        """
        Get the record hash from the smart contract storage
        :param key: unique key
        :return: hash
        """
        key_hash = hashlib.sha3_256(key.encode('utf-8'))
        return self.contract.functions.getHash(key_hash.digest()).call().hex()
