import hashlib
import struct

def double_sha256(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def target_from_bits(bits):
    """Calculate target integer from compact representation (bits)."""
    exponent = bits >> 24
    mantissa = bits & 0xffffff
    return mantissa * (1 << (8 * (exponent - 3)))

def mine_real_difficulty(difficulty_bits):
    # Example block header components (dummy data)
    version = struct.pack("<I", 2)
    prev_hash = b'\x00' * 32
    merkle_root = b'\x00' * 32
    timestamp = struct.pack("<I", 1231006505)
    bits = difficulty_bits
    nonce = 0

    target = target_from_bits(bits)
    print(f"Target: {hex(target)}")
    print("Mining started...")

    while nonce < 0xffffffff:
        nonce_bytes = struct.pack("<I", nonce)
        header = version + prev_hash + merkle_root + timestamp + struct.pack("<I", bits) + nonce_bytes
        hash_result = double_sha256(header)
        hash_int = int.from_bytes(hash_result[::-1], byteorder='big')
        
        if hash_int <= target:
            print("Found hash!")
            print("Nonce:", nonce)
            print("Hash:", hash_result[::-1].hex())
            break

        nonce += 1

    if nonce == 0xffffffff:
        print("Nonce range exhausted.")

if __name__ == "__main__":
    # Real Bitcoin difficulty bits for current network (~June 2025)
    # You'd replace this with the actual bits from the blockchain you want to simulate.
    real_difficulty_bits = 0x170db8ac  
    
    mine_real_difficulty(real_difficulty_bits)
