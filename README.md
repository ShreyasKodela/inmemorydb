# In-Memory DB with Transactions (Python)

This is a lightweight key-value store built in Python that supports basic transactions. It's kind of like a mini version of what you'd see behind money apps like Venmo. You can start a transaction, make changes with `put()`, and then either `commit()` or `rollback()` to apply or cancel them. Uncommitted changes stay hidden from regular `get()` calls. Only one transaction can run at a time.

## How to Run

1. Make sure Python 3.8+ is installed.

2. (Optional) Install `pytest` to run formal tests:
    pip install pytest

3. To run manual test output:
    python test_in_memory_db.py

4. To run all test cases with `pytest`:
    pytest


## How This Could Be Improved
- Add support for **nested transactions** and clarify expected behavior when they overlap.
- Provide **starter templates or a base class** so students can focus more on transaction logic.
- Include **automated edge-case tests** or a public test suite for instant feedback.

