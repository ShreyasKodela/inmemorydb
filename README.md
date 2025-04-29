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
 - Add support for checking if a transaction is active, such as an 'inTransaction()' method, to make debugging and usage clearer.
 - Provide starter code and a basic test harness to allow more focus on implementing transaction functionality.
 - Include edge-case examples and public test cases in the instructions to guide more thorough testing and catch potential issues early.

