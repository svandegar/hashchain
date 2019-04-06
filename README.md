# Hashchain  

## Introduction
`hashchain` is a Python package developed to join the ease of use of Python with the security of blockchain to certify that your important records haven't been tampered with. 

The core module creates a hash chain, attesting that no record can be tempered one saved. The blockchain module save a proof of your hashchain permanentely in the most secured way. Then, it's impossible to alter the haschain without causing a discrepancy with the blockchain.  

No need for third party certification anymore. No more single point of failure nor certification costs. 

## Installation
This python package is available on PyPi package manager. I recommend installing it in a [virtual environment](https://virtualenv.pypa.io/en/latest/).  
1. Open a terminal and run the following command : `pip install hashchain`
2. Import the package in you script with `import hashchain`

## How it works

## Warning
The package is still 'work in progress' Do not use it before the official beta release. All the features are still subject to changes without any advertisement and can broke previously running scripts 


## Changelog
#### 0.4.0
##### Features:
Add more precise feedback on Record.verify() errors

#### 0.3.0
##### Features:
Request.to_dict() and .to_json() now returns a simple object. The keys "hash" and "previous_hash" are appended at the same level

#####Fix: 
Add web3.py to the install_requires list

#### 0.2.0
##### Features:
Add records to build hash chains
Add ethereum_connector to store hashes on the Ethereum blockchain 

#### 0.1.0
First Alpha release. 
