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
    high_scores = top_keys(scores, 10)

    for k in high_scores:
        key = bytes(chr(k) * l, 'ascii')
        print(chr(k), scores[k], utils.xor_eq_buffers(key, text))


# There has to be a better way to do this
def top_keys(d, n):
    top = [0] * n
    for k, v in d.items():
        m = min(top)
        if v > d[m]:
            i = top.index(m)
            top[i] = k
    return top

if __name__ == '__main__':
    main()
