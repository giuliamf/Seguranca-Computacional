# https://github.com/giuliamf
# Author: Giulia Moura, 200018795
import string
# Elaborar o código que quebra a cifra por deslocamento
# 1. Distribuição de frequência de letras (frequency analysis)

from collections import Counter
from frequency_pt import frequency_portuguese


def frequency_analysis(text):
    text = text.upper()
    text_counter = Counter([char for char in text if char in string.ascii_uppercase])

    text_freq = {char: (count / len(text)) * 100 for char, count in text_counter.items()}

    best_k = 0
    best_diff = float('inf')
    decrypted_text = ''

    for k in range(26):
        shifted_counter = {}

        for char in text_freq:
            shifted_char = chr((ord(char) - ord('A') - k) % 26 + ord('A'))
            shifted_counter[shifted_char] = text_freq.get(char, 0)

        current_diff = sum(
            abs(shifted_counter.get(char, 0) - frequency_portuguese.get(char, 0)) for char in string.ascii_uppercase)

        if current_diff < best_diff:
            best_diff = current_diff
            best_k = k
            decrypted_text = ''.join(
                chr((ord(char) - ord('A') - best_k) % 26 + ord('A')) if char in string.ascii_uppercase else char
                for char in text
            )

    return decrypted_text, best_k
