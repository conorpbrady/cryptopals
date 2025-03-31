# CryptoPals Set 01 Challenge 06
#
# Break repeating key XOR
#
# The file s01_c06.txt is base64 data of a repeating key XOR
# Decrypt it


# We don't know the length of the key, loop through possible KEYSIZES (2 - 40)
#
# For each KEYSIZE (say 8), take the first block of (8) bytes, and the next
# block of (8) bytes and find the hamming distance between them
# Normalize by dividing by the KEYSIZE
#
# The smallest normalized edit distance is *probably* the actual keysize.
# Take 2-3 smallest and check
# -OR-
#  Take 4 keysize blocks and average the distances
#
# Now we should know the length of the key
#
# Break the ciphertext into keysize blocks
# Transpose the blocks - new_block = block[0][0] + block[1][0], etc
#
# Solve each transposed block and a single-char repeating XOR
# Put them together to get the key

import utils
import math
from base64 import b64decode
from itertools import combinations

# Average normalized hamming distance between a num of blocks
def avg_nhd(ciphertext, block_size, num_blocks):
    blocks = []
    for n in range(num_blocks):
        blocks.append(ciphertext[block_size * n: block_size * (n+1)])

    sum_nhd = 0
    combos = list(combinations([i for i in range(num_blocks)], 2))
    for c in combos:
        sum_nhd += utils.hamming_distance(blocks[c[0]], blocks[c[1]]) / block_size
    return sum_nhd / len(combos)

def main():
    ciphertext = b64decode(''.join(utils.read_file('s01_c06.txt')))
    potential_ks = [50, 50, 50]
    min_nhd = 1000
    min_ks = -1
    for ks in range(2, 40):
        block_a = ciphertext[:ks]
        block_b = ciphertext[ks: ks * 2]
        nhd = avg_nhd(ciphertext, ks, 8)
        # nhd = utils.hamming_distance(block_a, block_b) / ks
        if nhd < min_nhd:
            min_nhd = nhd
            min_ks = ks
    print(f'Probable keysize: {min_ks}')

    # Break up cipher text into blocks of size KEYSIZE
    c_blocks = [ciphertext[min_ks * n: min_ks * (n+1)] for n in range(math.floor(len(ciphertext) / min_ks))]

    # Transpose ciphertext blocks
    t_blocks = []
    for i in range(min_ks):
        t_block = b''
        for cb in c_blocks:
            t_block += bytes([cb[i]])

        t_blocks.append(t_block)

    # Find max score for repeating key xor against a single char
    max_scores = [0] * min_ks
    keys = [''] * min_ks

    for i in range(min_ks):
        scores = {}
        for j in range(128):
            l = len(t_blocks[i])
            key = bytes([j]) * l
            pt = utils.xor_eq_buffers(key, t_blocks[i])
            scores[j] = utils.score_characters(pt)

        max_score = 0
        max_k = ''
        for k, v in scores.items():
            if v > max_score:
                max_k = k
                max_score = v
        max_scores[i] = max_score
        keys[i] = max_k


    key = ''.join([chr(n) for n in keys])
    print(key)

    plaintext = b''
    c = 0
    for b in ciphertext:
        k = ord(key[c % len(key)])
        plaintext += bytes([b ^ k])
        c += 1
    print(plaintext)


if __name__ == '__main__':
    main()
