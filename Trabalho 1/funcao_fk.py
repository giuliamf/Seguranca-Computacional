from permutar import permutar
from xor import xor
from caixa_s import caixa_s


def funcao_fk(bits, subchave):
    ep = [4, 1, 2, 3, 2, 3, 4, 1]
    p4 = [2, 4, 3, 1]
    s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
    esquerda, direita = bits[:4], bits[4:]
    direita_expandida = permutar(direita, ep)
    resultado_xor = xor(direita_expandida, subchave)
    esquerda_caixa = caixa_s(resultado_xor[:4], s0)
    direita_caixa = caixa_s(resultado_xor[4:], s1)
    combinacao = esquerda_caixa + direita_caixa
    return xor(esquerda, permutar(combinacao, p4))
