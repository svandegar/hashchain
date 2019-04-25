Getting Started
===============

The hashchain library is a collection of module which contain specific functionality to certify data.

* ``records`` contains all the functions to hash records and build a hashchain in your database
* ``ethereum`` contains all the functions to deploy a smart contract on the Ethereum blockchain and interact with it.

See the Modules section for more details about these modules.

Installing hashchain
---------------------

This Python package is available on PyPi package manager. We recommend installing it in a `virtual environment <https://virtualenv.pypa.io/en/latest/>`_.

1. Open a terminal and run the following command : ``pip install hashchain``

2. Import the package in you script with ``import hashchain``

Ethereum blockchain requirements
--------------------------------

Even if this package provides all the tools to interact with the Ethereum blockchain, you will still need a few elements:

1. A wallet

There are many options to create an Ethereum wallet. My favorite is to use `Metamask <https://metamask.io/>`_ , which is a browser extension and allows you to use your wallet to login to dApps directly via your browser.
For testing purposes, you can create a wallet on the Ropsten test network, which works with fake money.

2. Some Ether

Every transaction on the Ethereum blockchain uses a certain amount of Ether, called gas. The price of the gas depends on the volume of transactions on the network and the amount needed for a transaction depends on the resources needed to execute it. You can buy Ether from $ on an exchange like `Coinbase <https://www.coinbase.com/>`_ . For testing purposes, enter your Ropsten wallet address on the `Ropsten Faucet <https://faucet.ropsten.be/>`_ to get free Ether.

3. An access to the Ethereum network

One option would be to run en Ethereum node but it's not easy and needs a certain amount of resources.

Using a connection provider like `Infura <https://infura.io/>`_ is the easiest and cheapest way to get instant access to the blockchain. You just need to register on their platform and get your Ethereum endpoint.

To use the ``hashchain`` package, you will need your wallet private and public key and the provider_url, which is your Ethereum endpoint




Voilà! You're now ready to use the ``hashchain`` package.