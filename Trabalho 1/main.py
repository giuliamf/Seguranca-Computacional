from gerar_chaves import gerar_chaves
from encriptar import encriptar
from decriptar import decriptar


if __name__ == '__main__':
    chave = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
    texto_claro = [1, 1, 0, 1, 0, 1, 1, 1]
    K1, K2 = gerar_chaves(chave)
    
    texto_original = texto_claro
    print('Texto Original:', texto_original)

    texto_cifrado = encriptar(texto_claro, K1, K2)
    print('Texto Cifrado:', texto_cifrado)

    texto_decriptado = decriptar(texto_cifrado, K1, K2)
    print('Texto Decriptado:', texto_decriptado)
    
    
