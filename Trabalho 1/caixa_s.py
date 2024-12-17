def caixa_s(bits, caixa):
    linha = (bits[0] << 1) | bits[3]
    coluna = (bits[1] << 1) | bits[2]
    valor = caixa[linha][coluna]
    return [int(b) for b in f'{valor:02b}']
