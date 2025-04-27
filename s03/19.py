# Break fixed-nonce CTR mode using substitutions
#
# Take your CTR encrypt/decrypt function, set the nonce to 0, and generate
# a random AES key

# In -successive encryptions- encrypt each line in 19.txt to produce
# multiple independent ciphertexts
#
# Each ciphertext has been encrypted against the same key stream
# so CT_BYTE xor PT_BYTE = KS_BYTE
# and CT_BYTE xor KS_BYTE = PT_BYTE
#
# Attack the cryptosystem - use letter frequencies, common english words, etc
#
# (This approach is sub-optimal, don't spend too much time here)

import sys
sys.path.append('..')
from cryptopals import CTR, CryptoPals as cp
from random import randbytes
import copy


def compare_top_scores(entries, n, new_entry):
    if len(entries.keys()) < n:
        return {**entries, **new_entry}
    m = min(entries, key=entries.get)
    s = next(iter(new_entry.values())) # Gets score of new_entry
    if s > entries[m]:
        entries.pop(m)
        entries = {**entries, **new_entry}
    return entries


def transpose(list_strs):
    ts = [x for x in zip(*list_strs)]
    o = []
    for t in ts:
        o.append(b''.join(bytes([x]) for x in t))
    return o

def main():
    plaintexts = cp.read_b64_file('19.txt', multiple_lines = True)
    ciphertexts = []
    key = randbytes(16)
    # Encrypt each plaintext using successive encryptions of CTR
    ciphertexts = [CTR(key).encrypt(pt) for pt in plaintexts]

    # The attack - the encrypted keystream will always use the same byte xored
    # against byte 0 of the ct - xor all 40 first bytes against all bytes
    # and see what appears to make the most sense?

    pkss = {b'': 0} # Potential Keystreams
    l = len(max(ciphertexts, key=len))

    for i in range(l):
        transposed = [c[:i+1] for c in ciphertexts if i < len(c)]
        prev_pkss = copy.deepcopy(pkss)
        for b in range(256):
            for ps in prev_pkss:
                g_ks = ps + bytes([b])
                guessed_plain_bytes = [cp.xor(tb, g_ks) for tb in transposed]
                d = {g_ks: cp.score_characters(b''.join(guessed_plain_bytes))}
                pkss = compare_top_scores(pkss, 3, d)
    m = max(pkss, key=pkss.get)
    print(cp.as_blocks(m, 16))
    print(b''.join([cp.xor(ct, m) for ct in ciphertexts]))


if __name__ == '__main__':
    main()
