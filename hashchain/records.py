import hashlib
import json


class Record():
    def __init__(self, content: dict, previous_hash: str = None):
        if not previous_hash:
            genesis = hashlib.sha3_256(b'0x0000000000000000000000000000000000000000000000000000000000000000')
            previous_hash = genesis.hexdigest()

        self.__content = json.dumps(content).encode('utf-8')
        self.__previous_hash = previous_hash
        self.__hash = hashlib.sha3_256()
        self.__hash.update(self.__content)
        self.__hash.update(previous_hash.encode('utf-8'))

    def __eq__(self, other: 'Record') -> bool:
        if self.get_hash() == other.get_hash():
            return True
        else:
            return False

    def get_hash(self) -> str:
        """
        Get the hex hash of the record
        :return: hex string
        """
        return self.__hash.hexdigest()

    def hex(self) -> str:
        """
        Get the hex hash of the record
        :return: hex string
        """
        return self.__hash.hexdigest()

    def get_content(self) -> dict:
        """
        Get the original content of the record
        :return: dict
        """
        return json.loads(self.__content.decode('utf-8'))

    def get_previous_hash(self) -> str:
        """
        Get the previous hash
        :return: hex string
        """
        return self.__previous_hash

    def update(self, new_content: dict):
        """
        Updates the record and recalculated the hash
        :param new_content: new record's content
        :return: None
        """
        self.__init__(new_content, self.__previous_hash)

    def to_dict(self) -> dict:
        """
        Return a dict of the complete record along with the hex string of the record's hash and the previous hash
        :return: dict
        """
        dict = self.get_content()
        dict['hash'] = self.get_hash()
        dict['previous_hash'] = self.get_previous_hash()
        return dict

    def to_json(self) -> str:
        """
        Returns the JSON of the complete record along with the hex string of the record's hash and the previous hash
        :return: JSON string
        """
        return json.dumps(self.to_dict())


class Chain():
    def __init__(self, content_dicts: list, last_hash: str = None):
        if last_hash:
            self.last_hash = last_hash
        else:
            self.last_hash = hashlib.sha3_256(
                b'0x0000000000000000000000000000000000000000000000000000000000000000').hexdigest()
        self.records = []
        for element in content_dicts:
            record = Record(element, self.last_hash)
            self.records.append(record)
            self.last_hash = record.get_hash()


def verify(records_dicts: list) -> bool:
    """
    Verifies a given list of records dicts
    :param records_dicts: list of Records objects
    :return: returns True if the list is valid. Raise ValueError if not valid.
    """
    for index, record in enumerate(records_dicts):
        content = {x : record[x] for x in record if x not in ['previous_hash','hash']}
        test_record = Record(content, record['previous_hash'])

        if record['hash'] != test_record.get_hash():
            raise ValueError('The record do no correspond to the hash provided')

        elif index >= 1 and test_record.get_previous_hash() != records_dicts[index - 1]['hash']:
            raise ValueError('The previous hash do no correspond to the hash of the previous element')

    return True
