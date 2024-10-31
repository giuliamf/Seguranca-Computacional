# Elaborar o código que quebra a cifra por deslocamento
# 2. Por ataque de força bruta (brute force)

def brute_force(cipher_text):
    for key in range(26):  
        decrypted_text = ''
        for char in cipher_text:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr((ord(char) - shift_base - key) % 26 + shift_base)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char

        if key == 3:
            return decrypted_text
