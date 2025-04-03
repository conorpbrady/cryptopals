LF = {'E' : 12.0, 'T' : 9.10, 'A' : 8.12, 'O' : 7.68, 'I' : 7.31,
      'N' : 6.95, 'S' : 6.28, 'R' : 6.02, 'H' : 5.92, 'D' : 4.32,
      'L' : 3.98, 'U' : 2.88, 'C' : 2.71, 'M' : 2.61, 'F' : 2.30,
      'Y' : 2.11, 'W' : 2.09, 'G' : 2.03, 'P' : 1.82, 'B' : 1.49,
      'V' : 1.11, 'K' : 0.69, 'X' : 0.17,'Q' : 0.11, 'J' : 0.10, 'Z' : 0.07,
      ' ': 15.00 }

def read_file(filename):
    output = []
    with open(filename, 'r') as f:
        output = [line.strip() for line in f.readlines()]
    return output


# Return XOR of two-equal length buffers
def xor_eq_buffers(a: bytes, b: bytes) -> bytes:
    result = b''
    for i in range(len(a)):
        # Friendly reminder:
        # bytes(3) returns b'\x00\x00\x00'
        # bytes([3]) returns b'\x03'
        result += bytes([a[i] ^ b[i]])
    return result

# Returns a score based of letter frequency.
# The higher the score, the more likely the string is an english phrase
def score_characters(s):
    score = 0
    for c in s:
        cc = chr(c).upper()
        if cc in LF:
            score += LF[cc]
    return score

# Find the number of differing bits between two byte strings
# TODO: Can't I just xor the characters and count the bits in the result?
# Rather than format to a binary string and comparing each bit
def hamming_distance(a: bytes, b: bytes) -> int:
    d = 0
    for i in range(len(a)):
        # Format each character as a binary string and compare bits
        ba = f'{a[i]:08b}'
        bb = f'{b[i]:08b}'
        for j in range(len(ba)):
            if ba[j] != bb[j]:
                d += 1
    return d
