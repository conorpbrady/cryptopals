# CryptoPals Set 02 Challenge 13
#
# ECB Cut and Paste
#
# Write a k=v parsing routine
#
# foo=bar&baz=qux&zap=zazzle
#
# Produces {'foo': 'bar', 'baz': qux', 'zap': 'zazzle'}
#
# Write a function that encodes a user profile in that format
#
# profile('foo@bar.com') produces email=foo@bar.com&id=10@role=user
#
# that function should now allow & or = characters in the email
#
# Generate a random AES key then
# A. Encrypt the encoded user profile, provide that to the 'attacker'
# B. Decrypt the encoded user profile and parse it

# Using only the profile function and the ciphertext, create a
# role=admin user

from Crypto.Cipher import AES

def pad(b, bs):
    pl = bs - (len(b) % bs)
    pad = bytes([pl]) * pl
    return b + pad

def as_blocks(s, l):
    return [s[i:i+l] for i in range(0, len(s), l)]
def decode(string):
    d = {}
    kv_pairs = string.split('&')
    for kv in kv_pairs:
        k, v = kv.split('=')
        d[k] = v
    return d

def encode(d):
    output = ''
    for k, v in d.items():
        output += f'{k}={v}&'
    return output[:-1] # Removes trailing &

def create_profile(email):
    sanitized = email.replace('=', '%3D').replace('&', '%26')
    return {'email': sanitized, 'uid': 10, 'role': 'user'}

def main():
    email = 'an_email@theperfectlength.com'
    profile = create_profile(email)
    profile_string = bytes(encode(profile), 'ascii')
    key = b'A'* 16
    cipher = AES.new(key, AES.MODE_ECB)
    ct = cipher.encrypt(pad(profile_string, len(key)))

    # How to attack
    # Create an email address of such length so that role= is at
    # the end of one block and 'user' is at the start of the next
    # Replace the 'user' + padding block with
    # 'admin' + padding
    new_block = cipher.encrypt(pad(b'admin', len(key)))
    ciphertext_blocks = as_blocks(ct, len(key))
    ciphertext_blocks[-1] = new_block
    ct = b''.join(ciphertext_blocks)
    print(cipher.decrypt(ct))

if __name__ == '__main__':
    main()
