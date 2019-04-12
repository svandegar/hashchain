from hashchain import records
import sha3
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

genesis_hash = sha3.keccak_256(b'0x0000000000000000000000000000000000000000000000000000000000000000').hexdigest()

d_previous_hash = sha3.keccak_256(b'foo').hexdigest()
e_previous_hash = sha3.keccak_256(b'bar').hexdigest()
f_previous_hash = sha3.keccak_256(b'foo').hexdigest()
g_previous_hash = sha3.keccak_256(b'foo').hexdigest()

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
    hash_a = sha3.keccak_256()
    hash_a.update(a_content.__str__().encode('utf-8'))
    hash_a.update(a_previous_hash.encode('utf-8'))


    # other Record
    hash_d = sha3.keccak_256()
    hash_d.update(d_content.__str__().encode('utf-8'))
    hash_d.update(d_previous_hash.encode('utf-8'))

    assert d.get_hash() == hash_d.hexdigest()


def test_Record_hex():
    assert a.hex() == 'ca28ead4df3a89b70668fd1edbce8726e9b5fd2b85276623076cbd3052017618'
    assert b.hex() == 'ca28ead4df3a89b70668fd1edbce8726e9b5fd2b85276623076cbd3052017618'
    assert c.hex() == '17f737c4c697c3c2aaf1ec87e8f2fdaf9a01b69a5d9524f095fef8d9ab11877d'
    assert d.hex() == '03b263483301730fec90813789c642da6557b5162a4c56e68a77d876e6789a0f'
    assert e.hex() == '7172f21051812a9f5da64171f9ec839223ba1aac5c128a6f0f54acda124d6da2'
    assert f.hex() == '03b263483301730fec90813789c642da6557b5162a4c56e68a77d876e6789a0f'
    assert g.hex() == '594522c7e61e3b6f215cda60c82fab544279a5bd3dbcf1bb7b92681d96c4e471'


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
    assert chain1.last_hash == '440f37efb581edf582f61e4d80d843fbf3b1c52e3e7f9c78d4505eeffdbdd2f1'

    chain2 = records.Chain([a_content, b_content, c_content, d_content], last_hash='foo')
    assert chain2.last_hash == '5b5c2f86ac2951502e76d0baa565cb5da87fe24c0f869f1d079977b16f598cc4'
