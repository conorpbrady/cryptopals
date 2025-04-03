# CryptoPals Set 02 Challenge 02
#
# Implement CBC Mode
#
# In CBC mode, each ciphertext block is added to the next plaintext block before the next call
# to the cipher core
#
# The first plaintext block is added to a 0th ciphertext block, (the IV)
#
# Implement CBC mode by hand by taking the ECB function - making it encrypt
# and using your XOR function to combine them
#
# The file c10.txt is intelligible when CBC decrypted against
# "YELLOW SUBMARINE" with an IV of all ASCII 0 \x00\x00\x00...

from base64 import b64decode
from Crypto.Cipher import AES

def b64_file(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    return b64decode(''.join(lines))

def xor(a, b):
    o = b''
    for i in range(len(a)):
        o += bytes([a[i] ^ b[i]])
    return o

def main():
    ct = b64_file('10.txt')
    iv = bytes([0]) * 16
    key = b"YELLOW SUBMARINE"
    ks = len(key)
    cipher = AES.new(key, AES.MODE_ECB)

    ct_blocks = [ct[i:i+ks] for i in range(0, len(ct), ks)]
    pt = b''

    for cb in ct_blocks:
        db = cipher.decrypt(cb)
        ptb = xor(iv, db)
        pt += ptb
        iv = cb

    print(pt)
if __name__ == '__main__':
    main()
