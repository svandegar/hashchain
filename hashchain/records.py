import hashlib
import json


class Record():
    def __init__(self, content: dict, previous_hash: hashlib.sha3_256() = None):

        if not previous_hash:
            previous_hash = hashlib.sha3_256()
            previous_hash.update(b'0x0000000000000000000000000000000000000000000000000000000000000000')

        self.__content = json.dumps(content).encode('utf-8')
        self.__previous_hash = previous_hash
        self.__hash = hashlib.sha3_256()
        self.__hash.update(self.__content)
        self.__hash.update(previous_hash.digest())

    def get_hash(self):
        return self.__hash.hexdigest()

    def hex(self):
        return self.__hash.hexdigest()

    def get_content(self):
        return json.loads(self.__content.decode('utf-8'))

    def get_previous_hash(self):
        return self.__previous_hash.hexdigest()

    def update(self, new_content: dict):
        self.__init__(new_content, self.__previous_hash)

    def __eq__(self, other: 'Record'):
        if self.get_hash() == other.get_hash():
            return True
        else:
            return False

    def to_dict(self):
        return dict(content=self.get_content(), hash=self.get_hash(), previous_hash=self.get_previous_hash())

    def to_json(self):
        return json.dumps(self.to_dict())

#
# class Chain():
#     def __init__(self, records_list: list):
#         for index, record in enumerate(records_list):
#             if record.get_previous_hash() != records_list[index - 1]:
#                 raise ValueError(f'The previous hash of the record located at the index {index} is not valid.')
#             if record.get_content():
#                 pass
