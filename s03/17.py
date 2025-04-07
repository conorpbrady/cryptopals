# CryptoPals Set 03 Challenge 17
#
# Write two functions
#
# The first function should take a random string out of 17.txt
# pad it, CBC encrypt it, provide the caller the ciphertext and iv
#
# The second function should consume the ciphertext, decrypt it
# check the padding and return true/false is the padding is valid or not
#
# The attack:
#
# Bitflip the last byte of the last block
# Unless the bit flip results in \x01, the oracle gives a padding error
# Retest with another bitflip to be sure
#
# Bitflip the second to last byte
# If you get a padding error, that's still valid padding
#
# Keep going until bitflipping a byte does not result in a padding error
# That is the last byte of the plaintext
#
# We know the padding length and padding byte, so now we bitflip the
# last byte of the plaintext and the padding bytes so that they are valid
# padding and the oracle doesn't give a padding error.
# That tells us what the last byte of the plaintext
#
# Repeat for the remaining bytes of the last block
#
# On the remaining blocks, you know there is no padding. Start the process
# over but start at changing the last byte of the block to \x01
