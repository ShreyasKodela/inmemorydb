from in_memory_db import InMemoryDB
import pytest

# Test committing a transaction applies changes
def test_commit_transaction():
    db = InMemoryDB()
    db.begin_transaction()
    db.put("X", 99)
    db.commit()
    assert db.get("X") == 99

# Test rolling back a transaction discards changes
def test_rollback_transaction():
    db = InMemoryDB()
    db.begin_transaction()
    db.put("Y", 50)
    db.rollback()
    assert db.get("Y") is None

# Test put() without a transaction raises an error
def test_put_without_transaction_raises():
    db = InMemoryDB()
    with pytest.raises(Exception, match="No transaction in progress"):
        db.put("Z", 123)

# Test commit() with no active transaction raises an error
def test_commit_without_transaction_raises():
    db = InMemoryDB()
    with pytest.raises(Exception, match="No transaction in progress"):
        db.commit()

# Test rollback() with no active transaction raises an error
def test_rollback_without_transaction_raises():
    db = InMemoryDB()
    with pytest.raises(Exception, match="No transaction in progress"):
        db.rollback()

# Test committing multiple keys in a single transaction
def test_multiple_keys_in_transaction():
    db = InMemoryDB()
    db.begin_transaction()
    db.put("A", 1)
    db.put("B", 2)
    db.commit()
    assert db.get("A") == 1
    assert db.get("B") == 2

# Test rollback after overwriting an existing committed value
def test_rollback_overwrite_existing_key():
    db = InMemoryDB()
    db.begin_transaction()
    db.put("C", 5)
    db.commit()
    db.begin_transaction()
    db.put("C", 10)
    db.rollback()
    assert db.get("C") == 5