# CryptoPals Set 02 Challenge 12
#
# Byte at a time ECB Decryption
#
# Create a function that encrpyts buffers under a *consistent*
# but *unknown* key
#
# Take that function and have it append to the plaintext the *unknown* string
# in 12.txt (b64decode it first)
#
# ecb_encrypt(your_string + unknown_string, random_key)
#
# You can decrypt unknown_string with repeated calls to the encrypt function

from base64 import b64decode
from Crypto.Cipher import AES
import random as r

def random_key(keysize):
    return r.randbytes(keysize)

KEY = random_key(16)

def pad(b, bs):
    pl = bs - (len(b) % bs)
    pad = bytes([pl]) * pl
    return b + pad


def read_b64_file(filename):
    with open(filename) as f:
        data = [l.strip() for l in f.readlines()]
    return b64decode(''.join(data))


def find_block_size():
    prev_ct = ''
    for i in range(2, 64):
        data = b'A' * i
        ct = ecb_encrypt(data)
        if ct[:4] == prev_ct[:4]:
            return i - 1
        prev_ct = ct
    return None

def ecb_encrypt(data):
    data = pad(data, len(KEY))
    c = AES.new(KEY, AES.MODE_ECB)
    return c.encrypt(data)

def is_ecb(ct, block_size):
    blocks = [ciphertext[i:i+block_size] for i in \
            range(0, len(ciphertext), block_size)]
    for b in blocks:
        c = blocks.count(b)
        if c != 1:
            return True
        return False

def main():

    unknown_string = read_b64_file('12.txt')
    key = random_key
    # 1. Feed identical bytes to the function 1 at a time
    # start with 'A' then 'AA', etc. Discover the block size
    # (even though we already know it)
    block_size = find_block_size()
    if block_size is None:
        print("Could not determine block size")
        return 0
    print(f'Block size: {block_size}')

    # 2. Detect that the function is using ECB
    # print(f'Using ECB: {is_ecb(data, block_size)}')

    # 3. Craft an input block 1 byte short of the block size
    input_block = b'A' * (block_size - 1)

    # 4. Make a dict of all possible values by feeding different strings
    # 'AAAAAAAB', 'AAAAAAAC', etc

    # 5. Match the output of the one-byte short input to the dict
    # We now know the first byte of the string

    # 6. Repeat for the next byte and so on

    # AAAx xxxx
    # AAKx xxxx
    # AKKx xxxx
    # KKKx xxxx
    unknown_blocks = [unknown_string[i:i+block_size] for i in \
            range(0, len(unknown_string), block_size)]
    known_blocks = []

    for j, ub in enumerate(unknown_blocks):
        known_bytes = b''
        while len(known_bytes) != len(ub):
            possible = {}
            for i in range(0, 256):

                prefix = b'A' * ((block_size) - \
                        (len(known_bytes) % block_size) - 1)

                pos_byte = bytes([i])
                pt = prefix + known_bytes + pos_byte

                ct = ecb_encrypt(pt)
                possible[ct] = pos_byte


            ct = ecb_encrypt(prefix + ub[:block_size - len(prefix)])

            known_bytes += possible[ct]

        known_blocks.append(known_bytes)

    print(b''.join(known_blocks))

if __name__ == '__main__':
    main()
