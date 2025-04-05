# CryptoPals Set 02 Challenge 14
#
# Byte at a time ECB decryption (harder)
#
# Same as challenge 12, but prepend a random number of random bytes
# i.e.
# encrypt(random_bytes + attacker_controlled + target_string)

# Same as challenge 12, but we find the number of random bytes by
# increasing the length of the attacker controlled string until the
# first block stops changing.
#
# Then disregard the first block, and solve as we did in challenge 12

def main():
    pass

if __name__ == '__main__':
    main()
