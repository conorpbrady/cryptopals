# CryptoPals Set 02 Challenge 15
#
# Write a function that takes plaintext, determines if it has
# pkcs7 padding, and strips it off. Throw an exception if it is not
# valid padding
#
# "ICE ICE BABY\x04\x04\x04\x04"
# ... has valid padding, and produces the result "ICE ICE BABY".
#
# The string:
#
# "ICE ICE BABY\x05\x05\x05\x05"
# ... does not have valid padding, nor does:
#
# "ICE ICE BABY\x01\x02\x03\x04"

class PaddingException(Exception):
    pass

def unpad(plaintext):
    lb = plaintext[-1]
    if plaintext[-1 * lb:] != bytes([lb]) * lb:
        raise PaddingException("Invalid PCKS7 Padding")
    return plaintext[:-1 * lb]
def main():
    valid     = b'ICE ICE BABY\x04\x04\x04\x04'
    invalid_1 = b'ICE ICE BABY\x05\x05\x05\x05'
    invalid_2 = b'ICE ICE BABY\x01\x02\x03\x04'

    print(unpad(valid))
    try:
        unpad(invalid_1)
    except PaddingException as e:
        print(e)
    try:
        unpad(invalid_2)
    except PaddingException as e:
        print(e)

if __name__ == '__main__':
    main()
