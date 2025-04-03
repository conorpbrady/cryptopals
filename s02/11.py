# CryptoPals Set 02 Challenge 11
#
# ECB / CBC detection oracle
#
# 1. Write a function to generate a random AES key - 16 random bytes
#
# 2. Write a function that encrypts data under an unknown key
#    - Prepend 5-10 bytes (random) and append 5-10 bytes to the plaintext
#    - Have the function encrypt using ECB half the time, and CBC the other
#    - Randomly decide which one to use
#
# 3. Detect the block cipher that is being used each time

from Crypto.Cipher import AES
import random

def xor(a, b):
    o = b''
    for i in range(len(a)):
        o += bytes([a[i] ^ b[i]])
    return o

def random_key(ks):
    return random.randbytes(ks)

def encrypt_ecb(key, data):
    c = AES.new(key, AES.ECB_MODE)
    return c.encrypt(data)

def encrypt_cbc(key, data):
    c = AES.new(key, AES.ECB_MODE)
    iv = random_key(len(key))
    pt_blocks = [data[i:i+len(key)] for i in range(0, len(data), len(key))]
    ciphertext = b''
    for pb in pt_blocks:
        x = xor(iv, pb)
        ct = c.encrypt(pb)
        iv = ct
        ciphertext += ct
    return ct

def encrypt(data):
    r = random.randint(0,2)
    k = random_key(16)
    # 0 ECB
    # 1 CBC
    if r == 0:
        ct = encrypt_ecb(k, data)
    else:
        ct = encrypt_cbc(k, data)
    return r, ct


def main():
    with open('11.txt') as f:
        data = ''.join([l.strip() for l in f.readlines()])
    print(data)

    # TODO: Run tests to make sure CBC Encryption works
    # TODO: Call mystery encrypt
    # TODO: Detect ECB Mode

if __name__ == '__main__':
    main()
