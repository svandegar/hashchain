from hashchain import records
import sha3
import pytest
import copy
import collections

# Set inputs

a_content = collections.OrderedDict({'a': 3})
b_content = collections.OrderedDict({'a': 3})
c_content = collections.OrderedDict({'c': 4})
d_content = collections.OrderedDict({'a': 3})
e_content = collections.OrderedDict({'a': 3})
f_content = collections.OrderedDict({'a': 3})
g_content = collections.OrderedDict({'c': 4})

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
    assert a.hex() == '1696beb08013f377b8ff15bfa86581a672eaff47ed61963602e8e8ac5c47f33b'
    assert b.hex() == '1696beb08013f377b8ff15bfa86581a672eaff47ed61963602e8e8ac5c47f33b'
    assert c.hex() == 'a93c283dd11c1a54efcebe517a00e075cd4b54f72d765d3ccf18f7283d854479'
    assert d.hex() == '0f2a20330548d8e51cac28b61352126c484f93a55cef2c59a624b636e059f389'
    assert e.hex() == '84f5224e4dcfbc670eae8c2fe5790c2538d5f73d6cfefb89e653af8f694a4aa8'
    assert f.hex() == '0f2a20330548d8e51cac28b61352126c484f93a55cef2c59a624b636e059f389'
    assert g.hex() == 'ce82ff457496fc3303848e53db24803cdf01fa4281cca3f74784118ca58d91b3'


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
    assert records.verify(chain_a[::-1]) == True

    with pytest.raises(ValueError):
        records.verify(chain_b[::-1])

    with pytest.raises(ValueError):
        records.verify(chain_c[::-1])


def test_Chain():
    chain1 = records.Chain([a_content, b_content, c_content, d_content])
    assert chain1.records.__len__() == 4
    assert chain1.last_hash == '18096f349b871c7c7d296b21f4a09c05e34358c4d3a23f588fa9172c92ef9593'

    chain2 = records.Chain([a_content, b_content, c_content, d_content], last_hash='foo')
    assert chain2.last_hash == '879a1946c10853b0ee29e609db4ea041ed829605651ecb54093375c6345cb1f7'
