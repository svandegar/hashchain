from hashchain import records
import hashlib
import json

# testing objects

a_content = {'a': 3}
b_content = {'a': 3}
c_content = {'c': 4}
d_content = {'a': 3}
e_content = {'a': 3}
f_content = {'a': 3}
g_content = {'c': 4}

genesis_hash = hashlib.sha3_256(b'0x0000000000000000000000000000000000000000000000000000000000000000')

d_previous_hash = hashlib.sha3_256(b'foo')
e_previous_hash = hashlib.sha3_256(b'bar')
f_previous_hash = hashlib.sha3_256(b'foo')
g_previous_hash = hashlib.sha3_256(b'foo')

a = records.Record(a_content)
b = records.Record(b_content)
c = records.Record(c_content)
d = records.Record(d_content, d_previous_hash)
e = records.Record(e_content, e_previous_hash)
f = records.Record(f_content, f_previous_hash)
g = records.Record(g_content, g_previous_hash)


def test_Record_get_hash():
    # first Record
    a_previous_hash = genesis_hash
    hash_a = hashlib.sha3_256()
    hash_a.update(json.dumps(a_content).encode('utf-8'))
    hash_a.update(a_previous_hash.digest())

    assert (a.get_hash() == hash_a.hexdigest())

    # other Record
    hash_d = hashlib.sha3_256()
    hash_d.update(json.dumps(d_content).encode('utf-8'))
    hash_d.update(d_previous_hash.digest())

    assert (d.get_hash() == hash_d.hexdigest())


def test_Record_hex():
    assert a.hex() == 'aee27503051c522b1664cc1761d994a3c6848bfe0467335e53c170c242a0e8d5'
    assert f.hex() == 'c2c7c6b6f2fbe5aa53792fa0d2b13a04ca90493652ca38b716f710b6627718e1'


def test_Record_get_content():
    assert a.get_content() == a_content
    assert b.get_content() == b_content
    assert c.get_content() == c_content
    assert d.get_content() == d_content
    assert e.get_content() == e_content
    assert f.get_content() == f_content
    assert g.get_content() == g_content


def test_Record_get_previous_hash():
    assert a.get_previous_hash() == genesis_hash.hexdigest()
    assert b.get_previous_hash() == genesis_hash.hexdigest()
    assert c.get_previous_hash() == genesis_hash.hexdigest()
    assert d.get_previous_hash() == d_previous_hash.hexdigest()
    assert e.get_previous_hash() == e_previous_hash.hexdigest()
    assert f.get_previous_hash() == f_previous_hash.hexdigest()
    assert g.get_previous_hash() == g_previous_hash.hexdigest()


def test_Record_eq__():
    assert (a == b)
    assert (a != c)
    assert (a != d)
    assert (d == f)
    assert (d != e)


def test_Record_update():
    assert (c != a)
    c.update(a_content)
    assert (c == a)

    assert (d != g)
    d.update(g_content)
    assert (d == g)


def test_Record_to_dict():
    assert a.to_dict() == dict(content=a_content,
                               hash=a.get_hash(),
                               previous_hash=a.get_previous_hash())


def test_Record_to_json():
    assert a.to_json() == json.dumps(dict(content=a_content,
                                          hash=a.get_hash(),
                                          previous_hash=a.get_previous_hash()))
