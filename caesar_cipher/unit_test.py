import caesar_cipher

# Encrypt 1
try:
    assert caesar_cipher.cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 23, 0) == "XYZABCDEFGHIJKLMNOPQRSTUVW"
except AssertionError:
    print("Error in Encrypt test case 1")

# Encrypt 2
try:
    assert caesar_cipher.cipher("ATTACKATONCE", 4, 0) == "EXXEGOEXSRGI"
except AssertionError:
    print("Error in Encrypt test case 2")

# Decrypt 1
try:
    assert caesar_cipher.cipher("XYZABCDEFGHIJKLMNOPQRSTUVW", 23, 1) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
except AssertionError:
    print("Error in Decrypt test case 1")

# Decrypt 2
try:
    assert caesar_cipher.cipher("EXXEGOEXSRGI", 4, 1) == "ATTACKATONCE"
except AssertionError:
    print("Error in Decrypt test case 2")
