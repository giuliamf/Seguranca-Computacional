# Gerador e Verificador de Assinaturas Digitais
Este projeto implementa um **Gerador e Verificador de Assinaturas Digitais** utilizando **RSA e OAEP**, garantindo a autenticidade e integridade de arquivos de texto. O sistema permite gerar chaves RSA, assinar mensagens e verificar assinaturas.

## **Funcionalidades**
- **Geração de Chaves RSA** (com teste de primalidade de Miller-Rabin)

- **Assinatura Digital** de mensagens com RSA e SHA-3

- **Verificação de Assinatura Digital** usando Base64

- **Uso de OAEP** para garantir maior segurança contra ataques

- Utilização de SHA3-256 para garantir integridade
  
## Descrição dos Arquivos

### 📂 **Código-Fonte (`src/`)**
- **`geradorVerificador.py`** → Arquivo principal, responsável por gerenciar o fluxo da aplicação (geração de chaves, assinatura e verificação).
- **`parte1.py`** → Contém a implementação da geração de chaves RSA, incluindo a criação de números primos e a função de hash SHA-3.
- **`parte2.py`** → Implementa a assinatura digital da mensagem, cifrando o hash da mensagem com a chave privada.
- **`parte3.py`** → Responsável pela verificação da assinatura digital, decifrando e comparando o hash com a mensagem original.
- **`documento.txt`** → Arquivo de texto que contém a mensagem a ser assinada e verificada.

### 📂 **Executável (`dist/`)**
- **`geradorVerificador.exe`** → Arquivo executável gerado pelo PyInstaller para execução sem necessidade do Python instalado.

### 📂 **Documentação (`docs/`)**
- **`Especificacoes_Seminario.pdf`** → Documento contendo as especificações do trabalho acadêmico.
- **`Relatório.pdf`** → Relatório detalhado sobre a implementação e funcionamento do sistema.
- **`Slides.pdf`** → Apresentação utilizada para demonstrar o projeto.

## **Requisitos**
- Python 3.8+
- Nenhuma biblioteca externa precisa ser instalada, pois o projeto utiliza apenas bibliotecas nativas do Python (`random`, `hashlib`, `os`, `math`, `base64`).

## Como Executar o Projeto

### 1️⃣ Rodando com Python
1. Clonar o Repositório
```bash 
git clone https://github.com/giuliamf/Seguranca-Computacional/tree/main/Seminário
cd Seminário/src
```
2. Executar o Script Principal
```bash 
python geradorVerificador.py
```

### 2️⃣ Executando o Arquivo `.exe` 
Se estiver no Windows, vá até a pasta `dist/` e execute:
```
cd dist
./geradorVerificador.exe
```
Ou clique duas vezes no `geradorVerificador.exe`

## Funcionamento
1. Geração das chaves RSA: O sistema gera um par de chaves (pública e privada).
2. Leitura da mensagem a partir do arquivo: A mensagem é carregada do ```documento.txt```.
3. Assinatura Digital: A mensagem é convertida em um hash SHA-3 e assinada com RSA.
4. Verificação da Assinatura: O documento assinado é verificado utilizando a chave pública RSA.
5. Validação da Integridade: O programa confirma se a assinatura corresponde à mensagem original.

## Referências
Criptografia RSA: [Veritas](https://www.veritas.com/pt/br/information-center/rsa-encryption), [Wikipedia](https://pt.wikipedia.org/wiki/RSA_(sistema_criptográfico))

SHA-3 (Secure Hash Algorithm 3): [Wikipedia](https://pt.wikipedia.org/w/index.php?title=SHA-3&oldid=66004885)

OAEP (Optimal Asymmetric Encryption Padding): [Medium](https://medium.com/asecuritysite-when-bob-met-alice/so-how-does-padding-work-in-rsa-6b34a123ca1f), [Wikipedia](https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding)

Miller-Rabin: [Geeks for Geeks](https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/)

## Autores
Projeto desenvolvido por [Giovanni Minari](https://github.com/GioLeiren), [Giulia Moura](https://github.com/giuliamf) e [Tiago Leão](https://github.com/TiagoBuson) para a disciplina Segurança Computacional na Universidade de Brasília (UnB).
