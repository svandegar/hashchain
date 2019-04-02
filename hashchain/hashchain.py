import hashlib
import json


class Record():
    def __init__(self, content: dict, previous_hash: hashlib.sha3_256() = None):
        self.__content = json.dumps(content).encode('utf-8')

        if not previous_hash:
            previous_hash = hashlib.sha3_256()
            previous_hash.update(b'0x0000000000000000000000000000000000000000000000000000000000000000')

        self.__previous_hash = previous_hash
        self.__hash = hashlib.sha3_256()
        self.__hash.update(self.__content)
        self.__hash.update(previous_hash.digest())

    def get_hash(self):
        return self.__hash


    def hex(self):
        return self.__hash.hexdigest()

    def get_content(self):
        return json.loads(self.__content.decode('utf-8'))

    def update(self, new_content: dict):
        self.__init__(new_content, self.__previous_hash)

    def __eq__(self, other : 'Record'):
        other_hash = other.get_hash()
        if self.__hash.digest() == other_hash.digest():
            return True
        else:
            return False




class Chain():
    def __init__(self, records_list: list):
        self.chain = []
        for record in records_list:
            self.chain.append(record.hash)
