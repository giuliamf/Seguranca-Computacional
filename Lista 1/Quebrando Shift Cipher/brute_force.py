import string


# Elaborar o código que quebra a cifra por deslocamento
# 2. Por ataque de força bruta (brute force)


def brute_force(cipher_text):
    for k in range(26):  # Tenta todos os deslocamentos possíveis
        decrypted_text = ''
        for char in cipher_text.upper():
            if char in string.ascii_uppercase:
                decrypted_text += chr((ord(char) - ord('A') - k) % 26 + ord('A'))
            else:
                decrypted_text += char

        if k == 3:
            return decrypted_text
