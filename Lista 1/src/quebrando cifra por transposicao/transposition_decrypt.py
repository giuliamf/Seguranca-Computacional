# Elaborar o código que quebra a cifra por transposição, descodificando por análises ao texto cifrado (CipherText-only)

from itertools import permutations
from frequency_pt import frequency_portuguese


def calculate_frequency(text):
    frequency = {chr(i): 0 for i in range(65, 91)}  # Letras maiúsculas A-Z
    for char in text.upper():
        if char in frequency:
            frequency[char] += 1

    total = sum(frequency.values())
    for letter in frequency:
        frequency[letter] = (frequency[letter] / total) * 100 if total > 0 else 0
    return frequency


def score_text(text):
    text_freq = calculate_frequency(text)
    return sum(abs(text_freq[letter] - frequency_portuguese[letter]) for letter in text_freq)


def transposition_decrypt(encrypted_text, key):
    num_columns = len(key)
    num_rows = len(encrypted_text) // num_columns

    columns = [''] * num_columns
    index = 0
    for col in sorted(range(num_columns), key=lambda x: key[x]):
        columns[col] = encrypted_text[index:index + num_rows]
        index += num_rows

    plaintext = ''
    for i in range(num_rows):
        for col in range(num_columns):
            plaintext += columns[col][i]

    return plaintext


def break_transposition(encrypted_text):
    best_score = float('inf')
    best_key = None
    best_decryption = ''

    for perm in permutations('31452'):
        decrypted_text = transposition_decrypt(encrypted_text, perm)
        score = score_text(decrypted_text)

        if score < best_score:
            best_score = score
            best_key = ''.join(perm)
            best_decryption = decrypted_text

    return best_key, best_decryption.rstrip('X')

