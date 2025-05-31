import hashlib
import time

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.transactions}{self.timestamp}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class PowerCurrencyBlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, [], int(time.time()), "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        index = len(self.chain)
        timestamp = int(time.time())
        previous_hash = self.get_latest_block().hash
        new_block = Block(index, transactions, timestamp, previous_hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Example usage
blockchain = PowerCurrencyBlockchain()

# Add some transactions
blockchain.add_block(["Alice produces 5 KWH", "Bob consumes 3 KWH"])
blockchain.add_block(["Charlie produces 2 KWH", "David consumes 1 KWH"])

# Print the blockchain
for block in blockchain.chain:
    print(f"Block #{block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Transactions: {block.transactions}")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print("\n")

# Validate the blockchain
print(f"Is blockchain valid? {blockchain.is_chain_valid()}")
