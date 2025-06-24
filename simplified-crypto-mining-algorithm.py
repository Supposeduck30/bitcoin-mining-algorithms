import hashlib
import struct
import random

def double_sha256(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def mine_block(difficulty):
    prefix = b'\x00' * difficulty
    version = struct.pack("<I", 2)
    prev_hash = b'\x00' * 32
    merkle_root = b'\x00' * 32
    timestamp = struct.pack("<I", 1231006505)
    bits = struct.pack("<I", 0x1d00ffff)

    print("Mining started... (random nonces)")

    attempts = 0
    tried_nonces = set()

    while True:
        nonce = random.randint(0, 0xffffffff)

        if nonce in tried_nonces:
            continue  
        tried_nonces.add(nonce)

        nonce_bytes = struct.pack("<I", nonce)
        header = version + prev_hash + merkle_root + timestamp + bits + nonce_bytes
        hash_result = double_sha256(header)

        if hash_result.startswith(prefix):
            print("Found hash!")
            print("Nonce:", nonce)
            print("Hash:", hash_result[::-1].hex())
            break

        attempts += 1
        if attempts % 1_000_000 == 0:
            print(f"Attempts: {attempts}... still mining")

if __name__ == "__main__":
    difficulty = random.randint(1,3) # Number of leading zero bytes
    mine_block(difficulty)
