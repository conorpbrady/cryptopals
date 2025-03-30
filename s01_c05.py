# CryptoPals Set 01 Challenge 05
#
# Implement repeating key XOR
#
# Encrypt the following phrase using repeating key XOR
# using the key ICE
#
#   Burning 'em, if you ain't quick and nimble
#   I go crazy when I hear a cymbal
#
# It should come out to:
#
#   0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
#   a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
#

def main():
    lines = [
            "Burning 'em, if you ain't quick and nimble\n",
            "I go crazy when I hear a cymbal"
            ]
    expected_results = [
            '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272',
            'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
            ]

    key = 'ICE'
    c = 0
    results = []
    for line in lines:
        result = b''

        lb = bytes(line, 'ascii')
        for b in lb:
            k = ord(key[c  % 3])
            result += bytes([b ^ k])
            c += 1
        results.append(result.hex())
    assert ''.join(results) == ''.join(expected_results)

if __name__ == '__main__':
    main()
