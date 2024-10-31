from frequency_analysis import break_cipher_frequency
from brute_force import brute_force
from shift_cipher import shift_cipher


def main():
    text = input('Digite o texto a ser cifrado: ')
    encrypted_text = shift_cipher(text, 3)
    print('Texto original: ' + text)
    print('Texto cifrado: ' + encrypted_text)
    print('Texto decifrado (por análise de frequência): ' + break_cipher_frequency(encrypted_text)[0])
    print('Texto decifrado (por força bruta):', brute_force(encrypted_text))


if __name__ == '__main__':
    main()
