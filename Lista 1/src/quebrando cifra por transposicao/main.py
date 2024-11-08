from transposition_encrypt import transposition_encrypt
from transposition_decrypt import break_transposition


def main():
    plaintext = input('Digite o texto a ser cifrado: ')
    encrypted_text = transposition_encrypt(plaintext, '31452')
    print('Texto original: ' + plaintext)
    print('Texto cifrado: ' + encrypted_text)

    # Tentativa de quebra da cifra
    best_key, decrypted_text = break_transposition(encrypted_text)
    print('Texto decifrado: ' + decrypted_text)
    print('Chave encontrada: ' + best_key)


if __name__ == '__main__':
    main()
