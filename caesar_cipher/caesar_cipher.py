# caesar_cipher.py

CHAR_SPACE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cipher(in_text, shift, mode):
	in_text = in_text.upper()
	
	shift = int(shift)
	out_text = ""


	for letter in in_text:
		
		# Encrypt mode
		if mode == 0:
			out_index = (CHAR_SPACE.index(letter) + shift) % 26
		
		# Decrypt mode
		elif mode == 1:
			out_index = (CHAR_SPACE.index(letter) - shift) % 26
		
		out_letter = CHAR_SPACE[out_index]
		#print(str(letter) + " --> " + str(ct_letter))
		
		out_text = out_text + out_letter
	
	return out_text
