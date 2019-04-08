from hashchain.ethereum.contract import EthContract
import json

# Set inputs
with open('./tests_inputs.json') as file:
    tests_inputs = json.load(file)

contract = EthContract()


# Tests
def test_EthContract_deploy():
    assert contract.deploy(
        sender_public_key=tests_inputs['sender_public_key'],
        sender_private_key=tests_inputs['sender_private_key'],
        provider_url=tests_inputs['provider_address']
    )


def test_get_txn_receipt():
    txn_hash = contract.deploy(
        sender_public_key=tests_inputs['sender_public_key'],
        sender_private_key=tests_inputs['sender_private_key'],
        provider_url=tests_inputs['provider_address']
    )
    assert contract.get_txn_receipt()