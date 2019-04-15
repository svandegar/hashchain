BYTECODE = r'0x608060405234801561001057600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555061029a806100606000396000f3fe608060405234801561001057600080fd5b5060043610610069576000357c0100000000000000000000000000000000000000000000000000000000900480633cf5040a1461006b5780638da5cb5b146100ad578063aca09e18146100f7578063cda1c3b914610139575b005b6100976004803603602081101561008157600080fd5b8101908080359060200190929190505050610171565b6040518082815260200191505060405180910390f35b6100b561018e565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6101236004803603602081101561010d57600080fd5b81019080803590602001909291905050506101b3565b6040518082815260200191505060405180910390f35b61016f6004803603604081101561014f57600080fd5b8101908080359060200190929190803590602001909291905050506101cb565b005b600060016000838152602001908152602001600020549050919050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60016020528060005260406000206000915090505481565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161461022457600080fd5b80600160008481526020019081526020016000208190555080827f072da75571c93893ebe214a98048832c37919c8e8a273de1e75e94ef9b99376760405160405180910390a3505056fea165627a7a723058200516396bf6d7796ea8542fbd1357a9668c4b1791c392bec5d56305e3153133110029'
ABI = r'''[
    {
      "constant": true,
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "",
          "type": "bytes32"
        }
      ],
      "name": "hashChain",
      "outputs": [
        {
          "name": "",
          "type": "bytes32"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "fallback"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "key",
          "type": "bytes32"
        },
        {
          "indexed": true,
          "name": "value",
          "type": "bytes32"
        }
      ],
      "name": "newHashRecorded",
      "type": "event"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "key",
          "type": "bytes32"
        },
        {
          "name": "value",
          "type": "bytes32"
        }
      ],
      "name": "record",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "key",
          "type": "bytes32"
        }
      ],
      "name": "getHash",
      "outputs": [
        {
          "name": "",
          "type": "bytes32"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    }
  ]
'''

