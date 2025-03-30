# CryptoPals Set 01 Challenge 03
#
# The hex encoded string,
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# has been XORed against a single character.
# Find the key, decrypt the message
import utils

def main():
    text = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    scores = {}
    l = len(text)
    for i in range(128):
        key = bytes(chr(i) * l, 'ascii')
        phrase = utils.xor_eq_buffers(key, text)
        scores[i] = utils.score_characters(phrase)

    max_score = 0
    max_k = ''
    for k, v in scores.items():
        if v > max_score:
            max_k = k
            max_score = v

    key = bytes(chr(max_k) * l, 'ascii')
    print(chr(max_k), max_score, utils.xor_eq_buffers(key, text))

if __name__ == '__main__':
    main()
