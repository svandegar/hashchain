Welcome to hashchain's documentation!
=====================================

.. toctree::
   :maxdepth: 3
   :caption: Contents:

    records<records>
    ethereum<ethereum>
    Solidity smart contract <solidity_contract>

Introduction
============
``hashchain`` is a Python package developed to join the ease of use of Python with the security of blockchain to certify that your important records haven't been tampered with.

The core module creates a hash chain, attesting that no record can be tempered with, once saved. The blockchain module save a proof of your hashchain permanentely in the most secured way. Then, it's impossible to alter the haschain without causing a discrepancy with the blockchain.

No need for third party certification anymore. No more single point of failure nor certification costs.

.. warning:: The package is still 'work in progress'
    Do not use it in production environment before the official release. All the features are still subject to changes without any advertisement and can broke previously running scripts



Installation
============

This python package is available on PyPi package manager. I recommend installing it in a `virtual environment <https://virtualenv.pypa.io/en/latest/>`_.

1. Open a terminal and run the following command : ``pip install hashchain``
2. Import the package in you script with ``import hashchain``

Usage
=====


