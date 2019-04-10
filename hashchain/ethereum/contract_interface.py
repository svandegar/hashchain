BYTECODE = r'0x608060405234801561001057600080fd5b5033600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506001600080600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff02191690831515021790555061061b806100da6000396000f3fe608060405260043610610083576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680633cf5040a146100925780636f324967146100e15780638da5cb5b1461014a578063aca09e18146101a1578063b6a5d7de146101f0578063cda1c3b914610241578063fe9fbb8014610286575b34801561008f57600080fd5b50005b34801561009e57600080fd5b506100cb600480360360208110156100b557600080fd5b81019080803590602001909291905050506102ef565b6040518082815260200191505060405180910390f35b3480156100ed57600080fd5b506101306004803603602081101561010457600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061030c565b604051808215151515815260200191505060405180910390f35b34801561015657600080fd5b5061015f61032c565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b3480156101ad57600080fd5b506101da600480360360208110156101c457600080fd5b8101908080359060200190929190505050610352565b6040518082815260200191505060405180910390f35b3480156101fc57600080fd5b5061023f6004803603602081101561021357600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061036a565b005b34801561024d57600080fd5b506102846004803603604081101561026457600080fd5b8101908080359060200190929190803590602001909291905050506104f2565b005b34801561029257600080fd5b506102d5600480360360208110156102a957600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061059a565b604051808215151515815260200191505060405180910390f35b600060026000838152602001908152602001600020549050919050565b60006020528060005260406000206000915054906101000a900460ff1681565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60026020528060005260406000206000915090505481565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610455576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252602b8152602001807f4f6e6c792074686520636f6e7472616374206f776e65722063616e206175746881526020017f6f72697a6520757365727300000000000000000000000000000000000000000081525060400191505060405180910390fd5b60016000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055508073ffffffffffffffffffffffffffffffffffffffff167f7d75ea9f22dff4328ed01edb890aca5758719cb05eb9a72be5e12ab4c660fc3860405160405180910390a250565b600115156000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16151514151561055057600080fd5b80600260008481526020019081526020016000208190555080827f072da75571c93893ebe214a98048832c37919c8e8a273de1e75e94ef9b99376760405160405180910390a35050565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff16905091905056fea165627a7a72305820f470201c67a218beb881a195c4b296819d88f3eb98fffa82e0a758c17d07ed0a0029'
ABI = r'''
[
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
      "type": "function",
      "signature": "0x6f324967"
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
      "type": "function",
      "signature": "0x8da5cb5b"
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
      "type": "function",
      "signature": "0xaca09e18"
    },
    {
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor",
      "signature": "constructor"
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
      "type": "event",
      "signature": "0x072da75571c93893ebe214a98048832c37919c8e8a273de1e75e94ef9b993767"
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
      "type": "event",
      "signature": "0x7d75ea9f22dff4328ed01edb890aca5758719cb05eb9a72be5e12ab4c660fc38"
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
      "type": "function",
      "signature": "0xb6a5d7de"
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
      "type": "function",
      "signature": "0xfe9fbb80"
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
      "type": "function",
      "signature": "0xcda1c3b9"
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
      "type": "function",
      "signature": "0x3cf5040a"
    }
  ]
'''

