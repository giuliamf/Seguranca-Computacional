# Elaborar o código que quebra a cifra por deslocamento
# 1. Distribuição de frequência de letras (frequency analysis)

from collections import Counter
from shift_cipher import shift_cipher
from frequency_pt import frequency_portuguese


def calculate_frequency(text):
    frequency = {}
    text_upper = text.upper()
    letters = [char for char in text_upper if char.isalpha()]
    count = Counter(letters)
    total = sum(count.values())

    for letter in frequency_portuguese.keys():  # Garante todas as letras
        frequency[letter] = (count.get(letter, 0) / total) * 100 if total > 0 else 0

    return frequency


def cipher_decrypt(cipher_text, k):
    return shift_cipher(cipher_text, -k)


def frequency_distance(fr1, fr2):
    letters = set(fr1.keys()).union(set(fr2.keys()))
    return sum(abs(fr1.get(letter, 0) - fr2.get(letter, 0)) for letter in letters)


def break_cipher_frequency(cipher_text):
    distance = float('inf')
    best_key = 0

    for key in range(26):
        decrypted_text = cipher_decrypt(cipher_text, key)
        frequency_decrypted = calculate_frequency(decrypted_text)
        current_distance = frequency_distance(frequency_decrypted, frequency_portuguese)

        if current_distance < distance:
            distance = current_distance
            best_key = key

    final_text = cipher_decrypt(cipher_text, best_key)
    return final_text, best_key
