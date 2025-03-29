LF = {'E' : 12.0, 'T' : 9.10, 'A' : 8.12, 'O' : 7.68, 'I' : 7.31,
      'N' : 6.95, 'S' : 6.28, 'R' : 6.02, 'H' : 5.92, 'D' : 4.32,
      'L' : 3.98, 'U' : 2.88, 'C' : 2.71, 'M' : 2.61, 'F' : 2.30,
      'Y' : 2.11, 'W' : 2.09, 'G' : 2.03, 'P' : 1.82, 'B' : 1.49,
      'V' : 1.11, 'K' : 0.69, 'X' : 0.17,'Q' : 0.11, 'J' : 0.10, 'Z' : 0.07 }

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
