# CryptoPals Set 02 Challenge 01
#
# PCK#7 Padding
# Pad any block to a specific block length; by appending the number of bytes of padding to the
# end of the block


def pkcs7_pad(b, bs):
    pl = bs - (len(b) % bs)
    pad = bytes([pl]) * pl
    return b + pad


def main():
    block = b"YELLOW SUBMARINE"
    result = b"YELLOW SUBMARINE\x04\x04\x04\x04"
    assert pkcs7_pad(block, 20) == result

if __name__ == '__main__':
    main()
