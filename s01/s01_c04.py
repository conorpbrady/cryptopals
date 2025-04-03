# CryptoPals Set 01 Challenge 04
#
# Detect single character XOR
#
# One of the 60 character strings in the file s01_c04.txt has
# been encrypted by a single character XOR. Find it

import utils

def main():
    lines = utils.read_file('s01_c04.txt')

    m = {'score': 0, 'index': -1, 'char': ''}
    for i, line in enumerate(lines):
        lb = bytes.fromhex(line)
        l = len(lb)
        for n in range(48, 128):
            key = bytes([n]) * l
            pt = utils.xor_eq_buffers(lb, key)
            score = utils.score_characters(pt)
            if score > m['score']:
                m = {'score': score, 'index': i, 'char': n}

    key = bytes([m['char']]) * l
    print(utils.xor_eq_buffers(key, bytes.fromhex(lines[m['index']])))


if __name__ == '__main__':
    main()
