from hashchain.ethereum import ethereum_connector
from hashchain import records
import json

# Set inputs
chain = records.Chain([{'foo':3},{'bar':4},{'foobar':'barfoo'}])

with open('hashchain/ethereum/Hashchain.json') as file:
    contract_json = json.load(file)

with open('hashchain/ethereum/tests/tests_inputs.json') as file:
    tests_inputs = json.load(file)


connector = ethereum_connector.EthConnector(
    contract_abi=json.dumps(contract_json['abi']),
    contract_address=tests_inputs['contract_address'] ,
    sender_public_key= tests_inputs['sender_public_key'],
    sender_private_key= tests_inputs['sender_private_key'],
    provider_address= tests_inputs['provider_address']
)


# Tests
def test_EthConnector_record():
    assert connector.record(chain.records[1].get_content()['bar'],chain.records[1].get_hash())

def test_EthConnector_getRecord():
    assert connector.getRecord(chain.records[1].get_content()['bar'])