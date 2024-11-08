# https://github.com/giuliamf
# Author: Giulia Moura, 200018795
import string


# Elaborar o código para realizar a cifra por deslocamento onde k = 3

def shift_cipher(text, k):
    encrypted_text = ''
    for char in text.upper():
        if char in string.ascii_uppercase:
            encrypted_text += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text
