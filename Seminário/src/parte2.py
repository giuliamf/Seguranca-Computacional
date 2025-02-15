from parte1 import generate_keys, encrypt, decrypt, HASH_FUNCTION


def sign_message(message, private_key):
    # Calcula o hash da mensagem
    hash_msg = HASH_FUNCTION(message.encode('utf-8'))

    # Cifra o hash com a chave privada
    signature = encrypt(hash_msg, private_key)

    return signature


def verify_signature(message, signature, public_key):
    # Calcula o hash da mensagem
    hash_msg = HASH_FUNCTION(message.encode('utf-8'))
    hash_int_original = int.from_bytes(hash_msg, 'big')

    # Decifra a assinatura usando a chave pública
    hash_signed = decrypt(signature, public_key)
    hash_int_signed = int.from_bytes(hash_signed, 'big')

    # Verifica se o hash calculado é igual ao hash da assinatura
    return hash_int_original == hash_int_signed
