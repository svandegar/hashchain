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

    def get_hash(self) -> str:
        return self.__hash.hexdigest()

    def hex(self) -> str:
        return self.__hash.hexdigest()

    def get_content(self) -> dict:
        return json.loads(self.__content.decode('utf-8'))

    def get_previous_hash(self) -> str:
        return self.__previous_hash

    def update(self, new_content: dict):
        self.__init__(new_content, self.__previous_hash)

    def __eq__(self, other: 'Record') -> bool:
        if self.get_hash() == other.get_hash():
            return True
        else:
            return False

    def to_dict(self) -> dict:
        return dict(content=self.get_content(), hash=self.get_hash(), previous_hash=self.get_previous_hash())

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


def verify(records_dicts: list) -> bool:
    """
    Verifies a given list of records dicts
    :param records_dicts: list of Records objects
    :return: returns True if the list is valid. Raise ValueError if not valid.
    """
    for index, record in enumerate(records_dicts):
        test_record = Record(record['content'], record['previous_hash'])

        if record['hash'] != test_record.get_hash():
            raise ValueError('The record do no correspond to the hash provided')

        elif index >= 1 and test_record.get_previous_hash() != records_dicts[index - 1]['hash']:
            raise ValueError('The previous hash do no correspond to the hash of the previous element')

    return True
