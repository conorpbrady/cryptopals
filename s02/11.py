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
from base64 import b64decode

def xor(a, b):
    o = b''
    for i in range(len(a)):
        o += bytes([a[i] ^ b[i]])
    return o

def random_key(ks):
    return random.randbytes(ks)

def pad(b, bs):
    pl = bs - (len(b) % bs)
    pad = bytes([pl]) * pl
    return b + pad

def encrypt_ecb(data, key):
    c = AES.new(key, AES.MODE_ECB)
    return c.encrypt(data)

def encrypt_cbc(data, key, iv = None):
    c = AES.new(key, AES.MODE_ECB)
    if iv is None:
        iv = random_key(len(key))
    pt_blocks = [data[i:i+len(key)] for i in range(0, len(data), len(key))]
    ciphertext = b''
    for pb in pt_blocks:
        x = xor(iv, pb)
        ct = c.encrypt(x)
        iv = ct
        ciphertext += ct
    return ciphertext


def detect_ecb(ciphertext, ks):
    blocks = [ciphertext[i:i+ks] for i in range(0, len(ciphertext), ks)]
    for b in blocks:
        c = blocks.count(b)
        if c != 1:
            return True
    return False

def encrypt(data):
    r = random.randint(0,1)
    k = random_key(16)
    # 1 ECB
    # 0 CBC
    if r == 1:
        ct = encrypt_ecb(data, k)
    else:
        ct = encrypt_cbc(data, k)
    return r, ct

def decrypt_cbc(ct, key, iv):
    c = AES.new(key, AES.MODE_ECB)
    ct_blocks = [ct[i:i+len(key)] for i in range(0, len(ct), len(key))]
    pt = b''
    for cb in ct_blocks:
        db = c.decrypt(cb)
        ptb = xor(iv, db)
        pt += ptb
        iv = cb
    return pt

def main():
    data = b'X' * 64

    # Make sure we implemented CBC encryption correctly
    ciphertext = encrypt_cbc(data, b"YELLOW SUBMARINE", bytes(16))
    plaintext = decrypt_cbc(ciphertext, b"YELLOW SUBMARINE", bytes(16))
    assert plaintext == data

    pre = random.randbytes(random.randint(5,10))
    post = random.randbytes(random.randint(5,10))
    data = pad(pre + data + post, 16)

    for i in range(10):
        method, ciphertext = encrypt(data)
        detected = 0
        if detect_ecb(ciphertext, 16):
            detected = 1
        print(method, detected)

if __name__ == '__main__':
    main()
