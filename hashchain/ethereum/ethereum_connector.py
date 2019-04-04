from web3 import Web3, HTTPProvider


class EthConnector():
    """
    Connector to interact with a smart contract on the Ethereum blockchain.
    """
    def __init__(self,
                 contract_abi: str,
                 contract_address: str,
                 sender_public_key: str,
                 sender_private_key: str,
                 provider_address: str):
        """

        :param contract_abi: smart contract's abi JSON string
        :param contract_address: smart contract address
        :param sender_public_key: public key of the sender
        :param sender_private_key: private key of the sender
        :param provider_address: address of the Ethereum connection provider
        """
        self._contract_abi = contract_abi
        self._contract_address = Web3.toChecksumAddress(contract_address)
        self._sender_public_key = Web3.toChecksumAddress(sender_public_key)
        self._sender_private_key = sender_private_key
        self._provider_address = provider_address
        self.w3 = Web3(HTTPProvider(self._provider_address))
        self.contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)

    def record(self, key: int, hash: str):
        """
        Records the key and hash in the smart contract storage
        :param key: indexed key, used to retrieve the hash
        :param hash: hash of the record
        :return: transaction hash
        """
        bytes_hash = bytes.fromhex(hash)
        txn_dict = dict(
            nonce=self.w3.eth.getTransactionCount(self._sender_public_key),
            gasPrice=self.w3.eth.gasPrice,
            gas=2000000
        )

        txn = self.contract.functions.record(key, bytes_hash).buildTransaction(txn_dict)
        signed_txn = self.w3.eth.account.signTransaction(txn, self._sender_private_key)
        return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    def getRecord(self, key: int):
        """
        Get the record hash from the smart contract storage
        :param key: unique key
        :return: hash
        """
        return self.contract.functions.getHash(key).call().hex()
