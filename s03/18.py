# Implement CTR Mode
#
# The string
# L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==
# decrypts to english when decrypted using CTR mode
#
# Key = YELLOW SUBMARINE
# Nonce = 0

from Crypto.Cipher import AES
from base64 import b64decode

def xor(a, b):
    output = b''
    for i in range(len(a)):
        output += bytes([ a[i] ^ b[i] ])
    return output

def ctr(text, key, nonce):
    blocks = [text[i:i+16] for i in range(0, len(text), 16)]
    counter = 0
    cipher = AES.new(key, AES.MODE_ECB)
    output = b''
    for b in blocks:
        ks = nonce.to_bytes(8, byteorder='little') + \
                counter.to_bytes(8, byteorder='little')
        print(ks)
        keystream = cipher.encrypt(ks)
        output += xor(b, keystream)
        counter += 1
    return output

def main():
    key = b'YELLOW SUBMARINE'
    nonce = 0

    ct = b64decode('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==')

    print(ctr(ct, key, nonce))


if __name__ == '__main__':
    main()
