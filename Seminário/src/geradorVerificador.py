import base64
from parte1 import HASH_FUNCTION, generate_keys
from parte2 import sign_message
from parte3 import verify_signed_document


if __name__ == "__main__":

    print("Gerando chaves RSA...")
    keys = generate_keys(key_size=1024)
    print("Chaves geradas com sucesso.")

    # Lendo a mensagem do arquivo
    try:
        with open("documento.txt", "r", encoding="utf-8") as file:
            original_message = file.read().strip()
        print(f"Mensagem lida do arquivo: {original_message}")
    except FileNotFoundError:
        print("Erro: O arquivo 'documento.txt' não foi encontrado.")
        exit(1)

    print("Gerando a assinatura da mensagem...")
    signature = sign_message(original_message, keys['private_key'])
    print(f"Assinatura gerada: {signature}")

    print("Formatando o documento assinado em Base64...")
    message_bytes = original_message.encode('utf-8')
    message_length_bytes = len(message_bytes).to_bytes(4, 'big')
    signature_bytes = signature.to_bytes((keys['public_key'][1].bit_length() + 7) // 8, 'big')

    signed_document = base64.b64encode(message_length_bytes + message_bytes + signature_bytes).decode('utf-8')
    print(f"Documento assinado formatado: {signed_document}")

    # Verifica o documento assinado
    is_valid, result = verify_signed_document(signed_document, keys['public_key'])

    if is_valid:
        print(f"A assinatura é válida. Mensagem original: {result}")
    else:
        print(f"A assinatura é inválida. Erro: {result}")

    input("------------------------------\n"
          "Pressione Enter para sair...")

