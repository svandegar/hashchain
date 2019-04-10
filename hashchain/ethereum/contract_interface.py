BYTECODE = r'0x608060405234801561001057600080fd5b5033600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506001600080600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055506105ae806100da6000396000f3fe608060405234801561001057600080fd5b506004361061009a576000357c010000000000000000000000000000000000000000000000000000000090048063aca09e1811610078578063aca09e1814610184578063b6a5d7de146101c6578063cda1c3b91461020a578063fe9fbb80146102425761009a565b80633cf5040a1461009c5780636f324967146100de5780638da5cb5b1461013a575b005b6100c8600480360360208110156100b257600080fd5b810190808035906020019092919050505061029e565b6040518082815260200191505060405180910390f35b610120600480360360208110156100f457600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506102bb565b604051808215151515815260200191505060405180910390f35b6101426102db565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6101b06004803603602081101561019a57600080fd5b8101908080359060200190929190505050610301565b6040518082815260200191505060405180910390f35b610208600480360360208110156101dc57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610319565b005b6102406004803603604081101561022057600080fd5b81019080803590602001909291908035906020019092919050505061045c565b005b6102846004803603602081101561025857600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610502565b604051808215151515815260200191505060405180910390f35b600060026000838152602001908152602001600020549050919050565b60006020528060005260406000206000915054906101000a900460ff1681565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60026020528060005260406000206000915090505481565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16146103bf576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252602b815260200180610558602b913960400191505060405180910390fd5b60016000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055508073ffffffffffffffffffffffffffffffffffffffff167f7d75ea9f22dff4328ed01edb890aca5758719cb05eb9a72be5e12ab4c660fc3860405160405180910390a250565b600115156000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff161515146104b857600080fd5b80600260008481526020019081526020016000208190555080827f072da75571c93893ebe214a98048832c37919c8e8a273de1e75e94ef9b99376760405160405180910390a35050565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905091905056fe4f6e6c792074686520636f6e7472616374206f776e65722063616e20617574686f72697a65207573657273a165627a7a7230582020e1afde3beaf863f8fdbe0d41d36e1645202b7d200b25314ac67c6e637435440029'
ABI = r'''
"abi": [
    {
      "constant": true,
      "inputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "name": "authorizedSenders",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
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
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "accountAddress",
          "type": "address"
        }
      ],
      "name": "authorizationGranted",
      "type": "event"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "user",
          "type": "address"
        }
      ],
      "name": "authorize",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "user",
          "type": "address"
        }
      ],
      "name": "isAuthorized",
      "outputs": [
        {
          "name": "authorized",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
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

