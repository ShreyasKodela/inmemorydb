from in_memory_db import InMemoryDB

db = InMemoryDB()

# Test 1: get() on non-existent key
print("1:", db.get("A"))  # None

# Test 2: put() without transaction should raise error
try:
    db.put("A", 5)
except Exception as e:
    print("2:", e)

# Test 3: put() during transaction doesn't affect visible state until committed
db.begin_transaction()
db.put("A", 5)
print("3:", db.get("A"))  # None

# Test 4: update value in transaction, then commit and confirm visibility
db.put("A", 6)
db.commit()
print("4:", db.get("A"))  # 6

# Test 5: commit with no active transaction should raise error
try:
    db.commit()
except Exception as e:
    print("5:", e)

# Test 6: rollback with no active transaction should raise error
try:
    db.rollback()
except Exception as e:
    print("6:", e)

# Test 7: get() on another non-existent key
print("7:", db.get("B"))  # None

# Test 8: put() in transaction then rollback, check if key is gone
db.begin_transaction()
db.put("B", 10)
db.rollback()
print("8:", db.get("B"))  # None

# Test 9: put() and commit a new key, then overwrite in new transaction and rollback
db.begin_transaction()
db.put("C", 100)
db.commit()
print("9:", db.get("C"))  # 100

db.begin_transaction()
db.put("C", 200)
db.rollback()
print("10:", db.get("C"))  # 100

# Test 11/12: try multiple puts in transaction before committing
db.begin_transaction()
db.put("D", 1)
db.put("E", 2)
db.commit()
print("11:", db.get("D"))  # 1
print("12:", db.get("E"))  # 2

# Test 13: begin transaction twice without committing should raise error
try:
    db.begin_transaction()
    db.begin_transaction()
except Exception as e:
    print("13:", e)
db.rollback()

# Test 14: commit with no changes should not affect state
db.begin_transaction()
db.commit()
print("14:", db.get("Z"))  # None

# Test 15: rollback without changes should not affect state
db.begin_transaction()
db.rollback()
print("15:", db.get("A"))  # 6
