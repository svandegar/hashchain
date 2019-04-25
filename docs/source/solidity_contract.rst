Solidity Contrat
================

Here is the Solidity contract definition built by the Python ``hashchain`` module.

This contract has been designed to store data privately using as little gas as possible.

This contract has been tested against `MythX <https://mythx.io/>`_ security standards.

.. code-block:: javascript 

    pragma solidity 0.5.7;

    contract Hashchain {

        // variables
        address  public  owner;
        mapping(bytes32 => bytes32)  public hashChain;

        // events
        event newHashRecorded(bytes32 indexed key, bytes32 indexed value);

        // constructor
        constructor() public {
            owner = msg.sender;
        }

        // functions
        function() external {}

        function record(bytes32 key, bytes32 value) external {
            require(msg.sender == owner);
            hashChain[key] = value;

            emit newHashRecorded(key, value);
        }

        function getHash(bytes32 key) external view returns (bytes32){
            return hashChain[key];
        }

    }

