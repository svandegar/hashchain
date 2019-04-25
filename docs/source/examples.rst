Examples of scripts using haschchain
========================================

Here are a few code samples showing the usage of the different modules from this package.

.. note::
    You can find a program used to demo this package on this repo: `https://github.com/svandegar/hashchain-demo <https://github.com/svandegar/hashchain-demo>`_

Records
--------

Implement a hash chain in a MongoDB database
********************************************
This script implements a hash chain, certifying data integrity in a database in a 7 lines of code.

.. code-block:: python
    :linenos:
    :emphasize-lines: 1,20-26

    from hashchain import records
    from datetime import datetime
    import pymongo
    import random

    # MongoDB connection
    MONGO_CONNECTION_STRING = os.environ.get('MONGO_CONNECTION_STRING')
    client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
    db = client['database-name']
    collection = db.collection

    # Build random data
    data = {
        'timestamp':datetime.now().replace(microsecond=0), # round to seconds to avoid problems due to MongoDB datetime precision limitation
        'sensorId':'ERDP-QT24', # dummy sensorId
        'value': random.random()
    }

    # Hash data along with the hash of the previous record
    try:
        last_record = collection.find({"sensorId": data['sensorId']}).sort([("timestamp", -1)])[0]
        last_record_hash = last_record['hash']

    except: # If this is the first record in the DB
        last_record_hash = None

    record = records.Record(data, last_record_hash)

    # Save the dictionary output of the record in the database
    collection.insert_one(record.to_dict())

Verify a hash chain from a MongoDB database
********************************************
This script verifies the integrity of an existing hash chain in a MongoDB database with two lines of code.

.. code-block:: python
    :linenos:
    :emphasize-lines: 1,17

    from hashchain import records
    import pymongo

    # MongoDB connection
    MONGO_CONNECTION_STRING = os.environ.get('MONGO_CONNECTION_STRING')
    client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
    db = client['database-name']
    collection = db.collection

    # Get the data form the DB
    chain = mongo_collection.find({'sensorId': 'ERDP-QT24'},
                                      {"_id": 0}).sort([("timestamp", -1)])

    db_records = list(chain)

    # Verify the chain validity
    records.verify(db_records)