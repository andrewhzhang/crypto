# caesar_cipher.py

CHAR_SPACE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plaintext, shift):
	plaintext = plaintext.upper()
	
	shift = int(shift)
	ciphertext = ""
	
	for letter in plaintext:
		ct_index = (CHAR_SPACE.index(letter) + shift) % 26
		ct_letter = CHAR_SPACE[ct_index]
		#print(str(letter) + " --> " + str(ct_letter))
		
		ciphertext = ciphertext + ct_letter
	
	return ciphertext


def decrypt(ciphertext, shift):
	ciphertext = ciphertext.upper()
	
	shift = int(shift)
	plaintext = ""
	
	for letter in ciphertext:
		pt_index = (CHAR_SPACE.index(letter) - shift) % 26
		pt_letter = CHAR_SPACE[pt_index]
		#print(str(letter) + " --> " + str(ct_letter))
		
		plaintext = plaintext + pt_letter
	
	return plaintext
