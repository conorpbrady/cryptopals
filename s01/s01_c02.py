# CryptoPals Set 01 Challenge 02
#
# Fixed XOR
#
# Write a function that takes two equal length buffers and produces their XOR combination

def xor_buffers(buf_a, buf_b):
    result = b''
    for i, byte in enumerate(buf_a):
        result += bytes([buf_a[i] ^ buf_b[i]])
    return result

def main():
    a = bytes.fromhex('1c0111001f010100061a024b53535009181c')
    b = bytes.fromhex('686974207468652062756c6c277320657965')
    expected_result = '746865206b696420646f6e277420706c6179'

    print(xor_buffers(a, b))
    assert expected_result == xor_buffers(a, b).hex()

if __name__ == '__main__':
    main()
