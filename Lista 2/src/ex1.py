from sympy import mod_inverse
import pandas as pd


def rsa_encrypt_decrypt(p, q, e, M):
    n = p * q
    phi_n = (p - 1) * (q - 1)

    d = mod_inverse(e, phi_n)
    C = pow(M, e, n)
    M_decrypted = pow(C, d, n)

    return {
        "n": n,
        "ϕ(n)": phi_n,
        "e": e,
        "d": d,
        "Encriptado (C)": C,
        "Decriptado (M)": M_decrypted
    }


exercises = [
    {"p": 3, "q": 11, "e": 7, "M": 5},
    {"p": 5, "q": 11, "e": 3, "M": 9},
    {"p": 7, "q": 11, "e": 17, "M": 8},
    {"p": 11, "q": 13, "e": 11, "M": 7},
    {"p": 17, "q": 31, "e": 7, "M": 2}
]

results = []
for idx, ex in enumerate(exercises, start=1):
    result = rsa_encrypt_decrypt(ex["p"], ex["q"], ex["e"], ex["M"])
    result["Exercício"] = f"(1-{chr(96 + idx)})"
    results.append(result)

results_df = pd.DataFrame(results)
print(results_df)


