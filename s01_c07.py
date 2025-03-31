# CryptoPals Set 01 Challenge 07
#
# AES in ECB Mode
#
# The base64 data in file s01_c07.txt has been encrypted via AES-128 in ECB
# mode with the key YELLOW SUBMARINE
#
# Decrypt it

from Crypto.Cipher import AES
import utils
from base64 import b64decode

def main():
    key = b'YELLOW SUBMARINE'

    ciphertext = b64decode(''.join(utils.read_file('s01_c07.txt')))
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext)



if __name__ == '__main__':
    main()
