# CryptoPal Set 01 Challenge 08
#
# Detect AES in ECB Mode
#
# In the s01_c08.txt file, there are a bunch of hex encoded ciphertext
# One of them has been encrypted with ECB
# Detect it
#
# Remember that the problem with ECB is that it is stateless and
# deterministic; the same 16 byte plaintext block will always
# produce the same 16 byte ciphertext
import utils

def main():
    bs = 16
    data = utils.read_file('s01_c08.txt')
    for i, line in enumerate(data):
        blocks = [line[i:i+bs] for i in range(0, len(line), bs)]
        for block in blocks:
            c = blocks.count(block)
            if c != 1:
                print(i, c,  ''.join(blocks))
                break
if __name__ == '__main__':
    main()
