# CryptoPals Set 02 Challenge 16
#
# CBC Bit FLipping attack
#
# Generate a random AES key
#
# The first function should take an arbitray string
# prepend "comment1=cooking%20MCs;userdata="
# and append ";comment2=%20like%20a%20pound%20of%20bacon"
#
# The function should quote out '=' and ';' characters
# Then pad out the string to a 16 byte block length and encrpyt it with AES
#
# The second function should decrypt the string and look for the characters
# ";admin=true;". Return true or false if the string exists

import sys
sys.path.append('..')
from cryptopals import CryptoPals
from Crypto.Cipher import AES
from random import randbytes

def encrypt_string(c, userdata):
    sanitized = userdata.replace('=', '%3D').replace(';', '%3B')
    plaintext = f'comment1=cooking%20MCs;userdata={sanitized}'
    plaintext += ";comment2=%20like%20a%20pound%20of%20bacon"
    padded = CryptoPals.pkcs7_pad(bytes(plaintext, 'ascii'), 16)
    return c.encrypt(padded)

def is_admin(c, ciphertext):
    plaintext = c.decrypt(ciphertext)
    if b';admin=true;' in plaintext:
        return True
    return False

def main():
    key = randbytes(16)
    c = AES.new(key, AES.MODE_CBC)
    userdata = ('X' * 16) + 'XXXXX:admin<true'
    ciphertext = encrypt_string(c, userdata)
    # First 2 blocks are the prepended string
    # Block 3 is where we can control the data
    # Have block 3 contain set data that where we modify the ciphertext
    # Block 4 has the admin=true bit, but with other characters that do
    # not get quoted by the first function
    ct = bytearray(ciphertext)
    ct[37] = ct[37] ^ 1
    ct[43] = ct[43] ^ 1
    ciphertext = bytes(ct)

    c = AES.new(key, AES.MODE_CBC)
    print(is_admin(c, ciphertext))

if __name__ == '__main__':
    main()
