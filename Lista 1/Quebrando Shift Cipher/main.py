# https://github.com/giuliamf
# Author: Giulia Moura, 200018795

from frequency_analysis import frequency_analysis
from brute_force import brute_force
from shift_cipher import shift_cipher


def main():
    plaintext = input('Digite o texto a ser cifrado: ')
    encrypted_text = shift_cipher(plaintext, 3)
    print('Texto original: ' + plaintext)
    print('Texto cifrado: ' + encrypted_text)
    print('Texto decifrado (por análise de frequência): ' + frequency_analysis(encrypted_text)[0])
    print('Texto decifrado (por força bruta):', brute_force(encrypted_text))


if __name__ == '__main__':
    main()
