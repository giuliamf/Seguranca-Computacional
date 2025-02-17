from OpenSSL import crypto

# Configurações do certificado
CERT_FILE = "cert.pem"
KEY_FILE = "key.pem"

# Criar uma chave privada
key = crypto.PKey()
key.generate_key(crypto.TYPE_RSA, 2048)

# Criar um certificado autoassinado
cert = crypto.X509()
cert.get_subject().C = "BR"  # País
cert.get_subject().ST = "Distrito Federal"  # Estado
cert.get_subject().L = "Brasília"  # Cidade
cert.get_subject().O = "UniversidadeDeBrasilia"  # Organização
cert.get_subject().OU = "CIC"  # Unidade Organizacional
cert.get_subject().CN = "localhost"  # Nome Comum

# Definir período de validade do certificado
cert.set_serial_number(1000)
cert.gmtime_adj_notBefore(0)  # Início da validade
cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)  # Expiração (1 ano)

# Associar a chave privada ao certificado
cert.set_issuer(cert.get_subject())
cert.set_pubkey(key)
cert.sign(key, "sha256")  # Assinar com SHA-256

# Salvar o certificado e a chave privada em arquivos
with open(CERT_FILE, "wb") as cert_file:
    cert_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

with open(KEY_FILE, "wb") as key_file:
    key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

print(f"Certificado '{CERT_FILE}' e chave privada '{KEY_FILE}' gerados com sucesso!")




