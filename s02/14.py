# CryptoPals Set 02 Challenge 14
#
# Byte at a time ECB decryption (harder)
#
# Same as challenge 12, but prepend a random number of random bytes
# i.e.
# encrypt(random_bytes + attacker_controlled + target_string)

# Same as challenge 12, but we find the number of random bytes by
# increasing the length of the attacker controlled string until the
# first block stops changing.
#
# Then disregard the first block, and solve as we did in challenge 12
import sys
sys.path.append('..')
import random as r
from cryptopals import CryptoPals as cp
from cryptopals import ECBOracle

def main():
    oracle = ECBOracle()
    target = cp.read_b64_file('12.txt')
    random_bytes = r.randbytes(r.randint(5, 10))
    block_size = cp.ecb_block_size(oracle)

    # Find # of random bytes
    # Limiting this to the block_size
    rand_length = 0
    prev_ct = ''
    for i in range(1, block_size):
        input_string = random_bytes + b'A' * i
        ct = oracle.encrypt(input_string)
        if ct[:4] == prev_ct[:4]:
            rand_length = block_size - (i - 1)
            break
        prev_ct = ct

    target_blocks = cp.as_blocks(target, block_size)
    known_blocks = []

    # We can only call the oracle as encrypt(rand + attack + target)
    # TODO: Don't process one block at a time
    # TODO: Increase pad unti we get a match
    # Loop through all prefix lengths
    # Check all blocks for a match
    # When it matches replace with found byte
    # Repeat?
    # TODO: Come back to this
    for tb in target_blocks:
        known_bytes = b''
        while len(known_bytes) != len(tb):
           # Generate dict of possible bytes
           # AAAAKKKx
            possible = {}
            attack = b'A' * (block_size - (len(known_bytes) % block_size) - 1)
            for i in range(0, 256):
                possible_byte = bytes([i])
                input_block = attack + known_bytes + possible_byte
                ciphertext = oracle.encrypt(input_block)
                possible[ciphertext] = possible_byte

            input_block = attack + tb[:block_size - len(attack)]

            ciphertext = oracle.encrypt(input_block)
            known_bytes += possible[ciphertext]

        known_blocks.append(known_bytes)

    print(b''.join(known_blocks))
if __name__ == '__main__':
    main()
