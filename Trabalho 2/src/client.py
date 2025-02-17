import requests
import urllib3

url = "https://localhost:4433"

# Ignorar avisos de SSL inseguros
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Enviar a requisição ignorando a verificação do certificado
response = requests.get(url, verify=False)

print(f"Resposta do servidor: {response.text}")


