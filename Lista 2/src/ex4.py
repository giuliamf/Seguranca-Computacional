from sympy import mod_inverse


def rsa_encrypt_decrypt_ascii(p, q, e, message):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)

    ascii_values = [ord(char) for char in message]

    encrypted_ascii = [pow(m, e, n) for m in ascii_values]
    encrypted_message = ''.join(chr(c) for c in encrypted_ascii)

    decrypted_ascii = [pow(c, d, n) for c in encrypted_ascii]
    decrypted_message = ''.join(chr(m) for m in decrypted_ascii)

    return {
        "n": n,
        "ϕ(n)": phi_n,
        "e": e,
        "d": d,
        "Mensagem original": message,
        "Valores encriptados": encrypted_ascii,
        "Mensagem encriptada": encrypted_message,
        "Valores decriptados": decrypted_ascii,
        "Mensagem decriptada": decrypted_message
    }


p, q, e = 11, 17, 7
message = "HELLO"

result_ex4 = rsa_encrypt_decrypt_ascii(p, q, e, message)
for item, result in result_ex4.items():
    print(f'{item} = {result}')
