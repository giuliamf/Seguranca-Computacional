from permutar import permutar
from deslocar_esquerda import deslocar_esquerda


def gerar_chaves(chave):
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]
    chave_permutada = permutar(chave, p10)
    esquerda, direita = chave_permutada[:5], chave_permutada[5:]
    esquerda = deslocar_esquerda(esquerda, 1)
    direita = deslocar_esquerda(direita, 1)
    K1 = permutar(esquerda + direita, p8)
    esquerda = deslocar_esquerda(esquerda, 2)
    direita = deslocar_esquerda(direita, 2)
    K2 = permutar(esquerda + direita, p8)
    return K1, K2
