import caesar_cipher

#plaintext = input("Please enter plaintext: ")
#shift = input("Enter shift key: ")

#print(caesar_cipher.encrypt(plaintext, shift))

try:
    assert caesar_cipher.encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 23) == "XYZABCDEFGHIJKLMNOPQRSTUVW"
except AssertionError:
    print("Error in test case 1")

try:
    assert caesar_cipher.encrypt("ATTACKATONCE", 4) == "EXXEGOEXSRGI"
except AssertionError:
    print("Error in test case 2")

try:
    assert caesar_cipher.decrypt("XYZABCDEFGHIJKLMNOPQRSTUVW", 23) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
except AssertionError:
    print("Error in test case 1")

try:
    assert caesar_cipher.decrypt("EXXEGOEXSRGI", 4) == "ATTACKATONCE"
except AssertionError:
    print("Error in test case 2")
