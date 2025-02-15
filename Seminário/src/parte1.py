import random
import hashlib
import os
from math import ceil


# Constants
HASH_FUNCTION = lambda x: hashlib.sha3_256(x).digest()
HASH_LENGTH = len(HASH_FUNCTION(b''))


def generate_large_prime(bits=1024):
    # Gera um número primo aleatório de 1024 bits e o testa pelo metodo de Miller-Rabin
    while True:
        candidate = random.getrandbits(bits)
        candidate |= (1 << bits - 1) | 1
        if miller_rabin_test(candidate):
            return candidate


def miller_rabin_test(n, k=20):
    # Teste probabilístico de primalidade de um número, usando iterações (20 como default)
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Função para calcular o inverso modular usando o Algoritmo de Euclides Extendido (mais rápido e eficiente)
def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


# Gerar par de chaves pública e privada para o RSA
def generate_keys(key_size=1024):
    p = generate_large_prime(key_size)
    q = generate_large_prime(key_size)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537  # Expoente público comumente usado
    d = modular_inverse(e, phi)
    
    return {
        'public_key': (e, n),
        'private_key': (d, n),
        "primes": (p, q)
    }


# Função de geração de máscara para DB e para a Seed
def mgf1(seed, length):
    if length > (2**32 * HASH_LENGTH):
        raise ValueError("Mask too long")
    
    T = b''
    for counter in range(ceil(length / HASH_LENGTH)):
        C = counter.to_bytes(4, 'big')
        T += HASH_FUNCTION(seed + C)
    return T[:length]


def oaep_pad(message, n):
    # Aplica padding OAEP à mensagem
    k = (n.bit_length() + 7) // 8  # Comprimento de n em bytes
    mLen = len(message)
    
    # Checagem de comprimento
    if mLen > k - 2 * HASH_LENGTH - 2:
        raise ValueError("Message too long")
    
    # Gera padding aleatório
    lHash = HASH_FUNCTION(b'')  # Hash da label vazia
    PS = b'\x00' * (k - mLen - 2 * HASH_LENGTH - 2)
    DB = lHash + PS + b'\x01' + message
    
    # Gera seed aleatória
    seed = os.urandom(HASH_LENGTH)
    
    # Mascara DB
    dbMask = mgf1(seed, k - HASH_LENGTH - 1)
    maskedDB = bytes(a ^ b for a, b in zip(DB, dbMask))
    
    # Mascara seed
    seedMask = mgf1(maskedDB, HASH_LENGTH)
    maskedSeed = bytes(a ^ b for a, b in zip(seed, seedMask))
    
    return b'\x00' + maskedSeed + maskedDB


def oaep_unpad(padded, n):
    # Remove padding OAEP da mensagem
    k = (n.bit_length() + 7) // 8
    
    # Checagem básica de formato
    if len(padded) != k:
        raise ValueError("Erro de decodificação")
    if padded[0] != 0:
        raise ValueError("Erro de decodificação")
    
    # Separa a mensagem
    maskedSeed = padded[1:HASH_LENGTH + 1]
    maskedDB = padded[HASH_LENGTH + 1:]
    
    # Recupera a seed
    seedMask = mgf1(maskedDB, HASH_LENGTH)
    seed = bytes(a ^ b for a, b in zip(maskedSeed, seedMask))
    
    # Recupera DB
    dbMask = mgf1(seed, k - HASH_LENGTH - 1)
    DB = bytes(a ^ b for a, b in zip(maskedDB, dbMask))
    
    # Verifica o padding
    lHash = HASH_FUNCTION(b'')
    if not DB.startswith(lHash):
        raise ValueError("Erro de decodificação")
    
    # Acha a mensagem
    i = HASH_LENGTH
    while i < len(DB):
        if DB[i] == 1:
            return DB[i + 1:]
        if DB[i] != 0:
            raise ValueError("Erro de decodificação")
        i += 1
    raise ValueError("Erro de decodificação")


def encrypt(message, public_key):
    # Encripta a mensagem usando RSA-OAEP
    e, n = public_key
    
    # Converte mensagem para bytes se é uma string
    if isinstance(message, str):
        message = message.encode('utf-8')
    
    # Aplica padding à mensagem
    padded = oaep_pad(message, n)
    
    # Converte para inteiro e encripta
    m_int = int.from_bytes(padded, 'big')
    c_int = pow(m_int, e, n)
    
    return c_int


def decrypt(ciphertext, private_key):
    # Decripta a mensagem usando RSA-OAEP
    d, n = private_key
    
    # Decripta
    m_int = pow(ciphertext, d, n)
    
    # Converte para bytes
    em = m_int.to_bytes((n.bit_length() + 7) // 8, 'big')
    
    # Tira o padding
    message = oaep_unpad(em, n)
    
    # Tenta decodificar como UTF-8 se possível
    try:
        return message.decode('utf-8')
    except UnicodeDecodeError:
        return message

