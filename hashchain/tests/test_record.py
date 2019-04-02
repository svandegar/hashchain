from hashchain import hashchain
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

d_previous_hash = b'foo'
e_previous_hash = b'bar'
f_previous_hash = b'foo'
g_previous_hash = b'foo'

a = hashchain.Record(a_content)
b = hashchain.Record(b_content)
c = hashchain.Record(c_content)
d = hashchain.Record(d_content, hashlib.sha3_256(d_previous_hash))
e = hashchain.Record(e_content, hashlib.sha3_256(e_previous_hash))
f = hashchain.Record(f_content, hashlib.sha3_256(f_previous_hash))
g = hashchain.Record(g_content, hashlib.sha3_256(g_previous_hash))


def test_Record_get_hash():
    # first Record
    previous_hash_a = hashlib.sha3_256()
    previous_hash_a.update(b'0x0000000000000000000000000000000000000000000000000000000000000000')
    hash_a = hashlib.sha3_256()
    hash_a.update(json.dumps({'a': 3}).encode('utf-8'))
    hash_a.update(previous_hash_a.digest())

    assert (a.get_hash().digest() == hash_a.digest())

    # other Record
    previous_hash_d = hashlib.sha3_256()
    previous_hash_d.update(b'foo')
    hash_d = hashlib.sha3_256()
    hash_d.update(json.dumps({'a': 3}).encode('utf-8'))
    hash_d.update(previous_hash_d.digest())

    assert (d.get_hash().digest() == hash_d.digest())


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