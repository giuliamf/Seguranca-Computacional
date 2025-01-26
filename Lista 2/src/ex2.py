from sympy import mod_inverse


def rsa_decrypt_intercepted(C, e, n):
    for i in range(2, n):
        if n % i == 0:
            p = i
            q = n // i
            break

    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)
    M = pow(C, d, n)

    return {
        "n": n,
        "ϕ(n)": phi_n,
        "e": e,
        "d": d,
        "Mensagem decriptada (M)": M
    }


C, e, n = 10, 5, 35
for item, result in rsa_decrypt_intercepted(C, e, n).items():
    print(f'{item} = {result}')
