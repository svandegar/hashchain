Solidity Contrat
================

Here is the Solidity contract definition built by the Python ``hashchain`` module. This contract has been tested against `MythX <https://mythx.io/>`_ security standards.

.. code-block:: javascript 

    pragma solidity 0.5.7;

    contract Hashchain {

        // variables
        mapping(address => bool)  public authorizedSenders;
        address  public  owner;
        mapping(bytes32 => bytes32)  public hashChain;


        // events
        event newHashRecorded(bytes32 indexed key, bytes32 indexed value);
        event authorizationGranted(address indexed accountAddress);


        // constructor
        constructor() public {
            owner = msg.sender;
            authorizedSenders[owner] = true;
        }


        // functions
        function() external {}

        function authorize(address user) public {
            require(msg.sender == owner, "Only the contract owner can authorize users");
            authorizedSenders[user] = true;

            emit authorizationGranted(user);
        }

        function isAuthorized(address user) external view returns (bool authorized){
            return authorizedSenders[user];
        }


        function record(bytes32 key, bytes32 value) external {
            require(authorizedSenders[msg.sender] == true);
            hashChain[key] = value;

            emit newHashRecorded(key, value);
        }

        function getHash(bytes32 key) external view returns (bytes32){
            return hashChain[key];
        }

    }

