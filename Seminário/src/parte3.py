import base64
from parte1 import HASH_FUNCTION
from parte2 import verify_signature


# parsing de um documento assinado formatado em Base64. Retorna a mensagem original e a assinatura como inteiros.
def parse_signed_document(signed_document):
    try:
        print("Iniciando o parsing do documento assinado.")
        # Decodifica o documento Base64
        decoded_data = base64.b64decode(signed_document)
        print("Documento decodificado de Base64 com sucesso.")

        # Divide a mensagem e a assinatura
        message_length = int.from_bytes(decoded_data[:4], 'big')
        print(f"Comprimento da mensagem extraído: {message_length} bytes.")

        message = decoded_data[4:4 + message_length].decode('utf-8')
        print(f"Mensagem extraída: {message}")

        signature = int.from_bytes(decoded_data[4 + message_length:], 'big')
        print(f"Assinatura extraída: {signature}")

        return message, signature
    except Exception as e:
        raise ValueError(f"Erro ao fazer o parsing do documento assinado: {e}")


# Verifica a validade de um documento assinado. Retorna um booleano e a mensagem original.
def verify_signed_document(signed_document, public_key):
    try:
        print("Iniciando a verificação do documento assinado...")
        # Parsing do documento assinado
        message, signature = parse_signed_document(signed_document)

        # Verifica a assinatura
        print("Verificando a assinatura...")
        is_valid = verify_signature(message, signature, public_key)
        print("Verificação da assinatura concluída.")
        return is_valid, message
    except ValueError as e:
        return False, str(e)
