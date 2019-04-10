from hashchain.ethereum.connector import EthConnector
from hashchain import records
import json

# Set inputs
chain = records.Chain([{'foo':3},{'bar':4},{'foobar':'barfoo'}])

with open('hashchain/ethereum/Hashchain.json') as file:
    contract_json = json.load(file)

with open('./tests_inputs.json') as file:
    tests_inputs = json.load(file)


connector = EthConnector(
    contract_abi=json.dumps(contract_json['abi']),
    contract_address=tests_inputs['contract_address'] ,
    sender_public_key= tests_inputs['sender_public_key'],
    sender_private_key= tests_inputs['sender_private_key'],
    provider_url= tests_inputs['provider_address']
)


# Tests
def test_EthConnector_record():
    assert connector.record(str(chain.records[1].get_content()),chain.records[1].get_hash())

def test_EthConnector_getRecord():
    assert connector.getRecord(str(chain.records[1].get_content()))