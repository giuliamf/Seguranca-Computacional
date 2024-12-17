from permutar import permutar
from funcao_fk import funcao_fk
from trocar import trocar


def encriptar(texto_claro, K1, K2):
    ip = [2, 6, 3, 1, 4, 8, 5, 7]
    ip_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    bits = permutar(texto_claro, ip)
    bits = funcao_fk(bits, K1) + bits[4:]
    bits = trocar(bits)
    bits = funcao_fk(bits, K2) + bits[4:]
    return permutar(bits, ip_inv)
