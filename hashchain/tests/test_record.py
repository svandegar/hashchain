from hashchain import records
import hashlib
import pytest
import copy

# Set inputs

a_content = {'a': 3}
b_content = {'a': 3}
c_content = {'c': 4}
d_content = {'a': 3}
e_content = {'a': 3}
f_content = {'a': 3}
g_content = {'c': 4}

genesis_hash = hashlib.sha3_256(b'0x0000000000000000000000000000000000000000000000000000000000000000').hexdigest()

d_previous_hash = hashlib.sha3_256(b'foo').hexdigest()
e_previous_hash = hashlib.sha3_256(b'bar').hexdigest()
f_previous_hash = hashlib.sha3_256(b'foo').hexdigest()
g_previous_hash = hashlib.sha3_256(b'foo').hexdigest()

a = records.Record(a_content)
b = records.Record(b_content)
c = records.Record(c_content)
d = records.Record(d_content, d_previous_hash)
e = records.Record(e_content, e_previous_hash)
f = records.Record(f_content, f_previous_hash)
g = records.Record(g_content, g_previous_hash)

chain_a = [
    records.Record(a_content).to_dict(),
    records.Record(b_content, records.Record(a_content).get_hash()).to_dict(),
    records.Record(c_content, records.Record(b_content, records.Record(a_content).get_hash()).get_hash()).to_dict()
]
chain_b = [
    records.Record(a_content).to_dict(),
    records.Record(b_content, records.Record(a_content).get_hash()).to_dict(),
    records.Record(c_content, genesis_hash).to_dict()
]
chain_c = [
    {'content': {'a': 4}, 'hash': '95fdffb09de2f3e3cea8b86da0748ca94d962090d35cd58d6865f860ac467a3e',
     'previous_hash': 'e611aee939484e3afa4ee9d9c4e23a004a1fe2805b7fa4c95d42f3f2667638a2'},
    records.Record(b_content, records.Record(a_content).get_hash()).to_dict(),
    records.Record(c_content, records.Record(b_content, records.Record(a_content).get_hash()).get_hash()).to_dict()
]


# Tests


def test_Record_get_hash():
    # first Record
    a_previous_hash = genesis_hash
    hash_a = hashlib.sha3_256()
    hash_a.update(a_content.__str__().encode('utf-8'))
    hash_a.update(a_previous_hash.encode('utf-8'))


    # other Record
    hash_d = hashlib.sha3_256()
    hash_d.update(d_content.__str__().encode('utf-8'))
    hash_d.update(d_previous_hash.encode('utf-8'))

    assert d.get_hash() == hash_d.hexdigest()


def test_Record_hex():
    assert a.hex() == 'd7874bdf8e874cdc24bccb2dfaaed24b88ea9dbebc0b2fae9f6e1bdf691115e2'
    assert b.hex() == 'd7874bdf8e874cdc24bccb2dfaaed24b88ea9dbebc0b2fae9f6e1bdf691115e2'
    assert c.hex() == '949553d53a9502131544a7865d3c2c518f41093d5e4c192075b8805f18436b87'
    assert d.hex() == '3098ef9fcfb55963d8670eec4dee23c58cfb0d0feef9dcf215f965483709fb51'
    assert e.hex() == 'c436a7b6bf29b798164e88795670a39ceb5bc3e4266f6c97a10db9dcf3a3b377'
    assert f.hex() == '3098ef9fcfb55963d8670eec4dee23c58cfb0d0feef9dcf215f965483709fb51'
    assert g.hex() == '0b485abe2315a3602178a1897f7c7eaa2f7de06100af8d74a6181bc7e0f80660'


def test_Record_get_content():
    assert a.get_content() == a_content
    assert b.get_content() == b_content
    assert c.get_content() == c_content
    assert d.get_content() == d_content
    assert e.get_content() == e_content
    assert f.get_content() == f_content
    assert g.get_content() == g_content


def test_Record_get_previous_hash():
    assert a.get_previous_hash() == genesis_hash
    assert b.get_previous_hash() == genesis_hash
    assert c.get_previous_hash() == genesis_hash
    assert d.get_previous_hash() == d_previous_hash
    assert e.get_previous_hash() == e_previous_hash
    assert f.get_previous_hash() == f_previous_hash
    assert g.get_previous_hash() == g_previous_hash


def test_Record_eq__():
    assert a == b
    assert a != c
    assert a != d
    assert d == f
    assert d != e


def test_Record_update():
    assert c != a
    c.update(a_content)
    assert c == a

    assert d != g
    d.update(g_content)
    assert d == g


def test_Record_to_dict():
    dict = copy.deepcopy(a_content)
    dict['hash'] = a.get_hash()
    dict['previous_hash'] = a.get_previous_hash()

    assert a.to_dict() == dict


def test_verify():
    assert records.verify(chain_a) == True

    with pytest.raises(ValueError):
        records.verify(chain_b)

    with pytest.raises(ValueError):
        records.verify(chain_c)


def test_Chain():
    chain1 = records.Chain([a_content, b_content, c_content, d_content])
    assert chain1.records.__len__() == 4
    assert chain1.last_hash == '7fcd65965419dc3ecdc9a30bbf16c0e59439056a5eaf9e50f413eb7b81c3c433'

    chain2 = records.Chain([a_content, b_content, c_content, d_content], last_hash='foo')
    assert chain2.last_hash == 'b66faeb799631c9565600fd5f7320027fd491df13c556003cc924cff88365833'
