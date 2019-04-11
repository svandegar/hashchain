# Hashchain  

## Introduction
`hashchain` is a Python package developed to join the ease of use of Python with the security of blockchain to certify that your important records haven't been tampered with. 

The core module creates a hash chain, attesting that no record can be tempered with, once saved. The blockchain module save a proof of your hashchain permanentely in the most secured way. Then, it's impossible to alter the haschain without causing a discrepancy with the blockchain.  

No need for third party certification anymore. No more single point of failure nor certification costs. 

## Disclaimer
The package is still 'work in progress' Do not use it before the official beta release. All the features are still subject to changes without any advertisement and can broke previously running scripts 


## Installation
This python package is available on PyPi package manager. I recommend installing it in a [virtual environment](https://virtualenv.pypa.io/en/latest/).  
1. Open a terminal and run the following command : `pip install hashchain`
2. Import the package in you script with `import hashchain`

## How to start using haschain? 
The documentation lives on [ReadTheDocs](https://hashchain.readthedocs.io/en/latest/)


## Contribute
I would be happy to hear from you if you have any comments, suggestions or requests to share with me. 

## Changelog
#### 0.7.0
##### Changes:
Removed every json conversion from the `records` module. /!\ This break previous versions. The hash calculation was impacted by this change.  

#### 0.6.2
##### Fixes:
* Updated the Ethereum contract to comply with [MythX](https://mythx.io/) security standards

#### 0.6.0
##### Features:
* Add `wait` argument to `ethereum.EthConnector().record()` to wait until the transaction receipt is received. This avoid sending many transactions with the same nonce, while running this function in a loop.

#### 0.5.0
##### Features:
* Updated the Ethereum Smart contract to store a `byte32=>byte32` key pair instead of `int64=>byte32`
* Updated `ethereum.EthContract().record()` and `ethereum.EthContract().record()` to take a string as key input instead of an int. The string is hashed and the hash is used as key on the blockchain.

#### 0.4.2
##### Fixes:
* Removed the contract JSON file fron the structure and added ethereum/contract_interface to get the contract abi and binary. 

#### 0.4.1
##### Fixes:
* Included the ethereum module in the package

#### 0.4.0
##### Features:
* Add more precise feedback on Record.verify() errors
* Add ethereum.EthContract() to enable deploying the solidity smart contract on the Ethereum blockchain

#### 0.3.0
##### Features:
Request.to_dict() and .to_json() now returns a simple object. The keys "hash" and "previous_hash" are appended at the same level

#####Fix: 
Add web3.py to the install_requires list

#### 0.2.0
##### Features:
* Add records to build hash chains
* Add ethereum_connector to store hashes on the Ethereum blockchain 

#### 0.1.0
First Alpha release. 
