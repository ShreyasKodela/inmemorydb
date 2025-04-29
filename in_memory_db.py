class InMemoryDB:
    def __init__(self):
        # Stores the committed key-value pairs
        self.data = {}
        # Temporarily holds changes during a transaction
        self.transaction = None
        # Flag to track if a transaction is active
        self.in_transaction = False

    # Returns the committed value for a key (ignores uncommitted changes)
    def get(self, key):
        if self.in_transaction and key in self.transaction:
            return None
        return self.data.get(key, None)

    # Stages a key-value change (only allowed within an active transaction)
    def put(self, key, value):
        if not self.in_transaction:
            raise Exception("No transaction in progress")
        self.transaction[key] = value

    # Starts a new transaction
    def begin_transaction(self):
        if self.in_transaction:
            raise Exception("Transaction already in progress")
        self.transaction = {}
        self.in_transaction = True

    # Commits all staged changes to the main data store
    def commit(self):
        if not self.in_transaction:
            raise Exception("No transaction in progress")
        self.data.update(self.transaction)
        self.transaction = None
        self.in_transaction = False

    # Discards all changes made during the current transaction
    def rollback(self):
        if not self.in_transaction:
            raise Exception("No transaction in progress")
        self.transaction = None
        self.in_transaction = False
