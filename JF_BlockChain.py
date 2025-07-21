import hashlib           # For generating block hashes using SHA-256
import time              # To timestamp each block
import json              # To save the blockchain as a JSON file

# 🧱 Block class: defines structure and mining process
class Block:
    def __init__(self, index, data, previous_hash, difficulty=3):
        self.index = index                             # Block number
        self.timestamp = time.time()                   # Time of creation
        self.data = data                               # Custom user data
        self.previous_hash = previous_hash             # Hash of the previous block
        self.nonce = 0                                 # Counter used in PoW
        self.difficulty = difficulty                   # Difficulty level for mining
        self.hash = self.mine_block()                  # Generate hash by mining

    def mine_block(self):
        target = '0' * self.difficulty                 # Target prefix for valid hash (e.g. '000')
        while True:
            # Concatenate block data as string for hashing
            block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
            block_hash = hashlib.sha256(block_content.encode()).hexdigest()   # Create SHA-256 hash

            if block_hash.startswith(target):          # Check if hash meets difficulty
                return block_hash                      # Return valid hash

            self.nonce += 1                            # Increment nonce and retry

    def to_dict(self):
        # Convert block data into dictionary format for saving to JSON
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "hash": self.hash
        }

# ⛓ Blockchain class: manages chain and file storage
class Blockchain:
    def __init__(self, filename="blockchain_data.json"):
        self.chain = [self.create_genesis_block()]     # Initialize chain with Genesis block
        self.difficulty = 3                            # Difficulty setting
        self.filename = filename                       # Output file name
        self.write_chain_to_file()                     # Save initial chain to file

    def create_genesis_block(self):
        # Create the first block in the chain
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        # Add a new block with user-provided data
        prev_block = self.chain[-1]                    # Get the last block
        new_block = Block(len(self.chain), data, prev_block.hash, self.difficulty)  # Create new block
        self.chain.append(new_block)                   # Append new block to chain
        self.write_chain_to_file()                     # Save updated chain to file

    def write_chain_to_file(self):
        # Write the blockchain to a JSON file
        with open(self.filename, 'w') as file:
            json.dump([block.to_dict() for block in self.chain], file, indent=4)

# 🚀 Run the blockchain program interactively
if __name__ == "__main__":
    my_chain = Blockchain()                            # Create a blockchain instance

    while True:
        # Prompt user for input data
        user_input = input("🔹 Enter data to store in blockchain (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':               # Exit condition
            print("Blockchain saved. Goodbye! 🚀")
            break

        my_chain.add_block(user_input)                 # Add block with user input
        print(f"✅ Block added: {user_input}")          # Confirmation message