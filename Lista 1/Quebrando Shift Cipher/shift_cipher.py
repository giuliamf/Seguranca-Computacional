# Elaborar o código para realizar a cifra por deslocamento onde k = 3

def shift_cipher(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + k - 65) % 26 + 65)
            else:
                result += chr((ord(char) + k - 97) % 26 + 97)
        else:
            result += char
    return result
