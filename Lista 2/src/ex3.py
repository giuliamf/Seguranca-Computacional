from sympy import mod_inverse


def rsa_encrypt_decrypt_binary(p, q, e, binary_message):
    decimal_message = int(binary_message, 2)

    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)

    encrypted_decimal = pow(decimal_message, e, n)
    decrypted_decimal = pow(encrypted_decimal, d, n)

    encrypted_binary = bin(encrypted_decimal)[2:]
    decrypted_binary = bin(decrypted_decimal)[2:].zfill(len(binary_message))

    return {
        "n": n,
        "ϕ(n)": phi_n,
        "e": e,
        "d": d,
        "Mensagem original (binário)": binary_message,
        "Mensagem original (decimal)": decimal_message,
        "Mensagem encriptada (binário)": encrypted_binary,
        "Mensagem encriptada (decimal)": encrypted_decimal,
        "Mensagem decriptada (binário)": decrypted_binary,
        "Mensagem decriptada (decimal)": decrypted_decimal
    }


p, q, e = 11, 23, 3
binary_message = "0111001"
result_ex3 = rsa_encrypt_decrypt_binary(p, q, e, binary_message)

for item, result in result_ex3.items():
    print(f'{item} = {result}')

