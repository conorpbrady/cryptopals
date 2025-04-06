from base64 import b64decode, b64encode
from Crypto.Cipher import AES
import random as r

class CryptoPals:

    @staticmethod
    def xor(a, b):
        o = b''
        for i in a:
            o += bytes([a[i] ^ b[i]])
        return o

    @staticmethod
    def pkcs7_pad(s, size):
        pl = size - (len(s) % size)
        pad = bytes([pl]) * pl
        return s + pad

    @staticmethod
    def random_key(keysize):
        return r.randbytes(keysize)

    @staticmethod
    def ecb_block_size(cipher):
        prev_ct = ''
        for i in range(2, 64):
            data = b'A' * i
            ct = cipher.encrypt(data)
            if ct[:4] == prev_ct[:4]:
                return i - 1
            prev_ct = ct
        return None

    @staticmethod
    def as_blocks(s, n):
        return [s[i:i+n] for i in range(0, len(s), n)]

    @staticmethod
    def read_b64_file(filename):
        with open(filename) as f:
            data = [l.strip() for l in f.readlines()]
        return b64decode(''.join(data))

class ECBOracle:

    def __init__(self, key = None):
        if key is None:
            key = CryptoPals.random_key(16)
        self.key = key
        self.cipher = AES.new(key, AES.MODE_ECB)

    def pkcs7_pad(self, s, size):
        pl = size - (len(s) % size)
        pad = bytes([pl]) * pl
        return s + pad

    def encrypt(self, data):
        padded = self.pkcs7_pad(data, len(self.key))
        return self.cipher.encrypt(padded)
