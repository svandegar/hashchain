from hashchain import records
import hashlib
import json
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
    {'content': {'a': 4}, 'hash': '95fdffb09de2f3e3cea8b86da0748ca94d962090d35cd58d6865f860ac467a3e', 'previous_hash': 'e611aee939484e3afa4ee9d9c4e23a004a1fe2805b7fa4c95d42f3f2667638a2'},
    records.Record(b_content, records.Record(a_content).get_hash()).to_dict(),
    records.Record(c_content, records.Record(b_content, records.Record(a_content).get_hash()).get_hash()).to_dict()
]

# Tests


def test_Record_get_hash():
    # first Record
    a_previous_hash = genesis_hash
    hash_a = hashlib.sha3_256()
    hash_a.update(json.dumps(a_content).encode('utf-8'))
    hash_a.update(a_previous_hash.encode('utf-8'))

    assert a.get_hash() == hash_a.hexdigest()

    # other Record
    hash_d = hashlib.sha3_256()
    hash_d.update(json.dumps(d_content).encode('utf-8'))
    hash_d.update(d_previous_hash.encode('utf-8'))

    assert d.get_hash() == hash_d.hexdigest()


def test_Record_hex():
    assert a.hex() == '95fdffb09de2f3e3cea8b86da0748ca94d962090d35cd58d6865f860ac467a3e'
    assert b.hex() == '95fdffb09de2f3e3cea8b86da0748ca94d962090d35cd58d6865f860ac467a3e'
    assert c.hex() == 'ff7f75c77ae32fa60c4bc19d86adfb2e93d63f710ddfa297833ba5c75553dbf6'
    assert d.hex() == 'a7493b931d82f592a10e3b5759a214f18f1d7ef054bac50e220807f831595d6c'
    assert e.hex() == 'da99cfd956ac1db6f67722e1907be703aa21da69977abedb621fb469c682a85a'
    assert f.hex() == 'a7493b931d82f592a10e3b5759a214f18f1d7ef054bac50e220807f831595d6c'
    assert g.hex() == '93be4678ab7ce6895ee63d9d557f170adadb21dfd217cc9b742a311c8d4d6007'


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
    dict['hash']=a.get_hash()
    dict['previous_hash'] = a.get_previous_hash()

    assert a.to_dict() == dict


def test_Record_to_json():
    dict = copy.deepcopy(a_content)
    dict['hash'] = a.get_hash()
    dict['previous_hash'] = a.get_previous_hash()

    assert a.to_json() == json.dumps(dict)


def test_verify():
    assert records.verify(chain_a) == True

    with pytest.raises(ValueError) :
        records.verify(chain_b)

    with pytest.raises(ValueError) :
        records.verify(chain_c)


def test_Chain():
   chain1 = records.Chain([a_content,b_content,c_content,d_content])
   assert chain1.records.__len__() == 4
   assert chain1.last_hash == '4065526ceb951b5aa5bf1392cb5611275091f1dcd87c2842fcc2379ef9606c2f'

   chain2 = records.Chain([a_content, b_content, c_content, d_content], last_hash='foo')
   assert chain2.last_hash =='cbf4c24a816500cee4c0ed556775b14bf12369cba31c3fb1aa6faef132a1a79e'
