def deslocar_esquerda(bits, deslocamentos):
    return bits[deslocamentos:] + bits[:deslocamentos]
