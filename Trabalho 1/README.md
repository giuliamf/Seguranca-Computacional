# Projeto de Implementação do S-DES

## Descrição

Este projeto implementa o algoritmo Simplified Data Encryption Standard (S-DES), uma versão simplificada do DES usada para fins educacionais. Ele utiliza uma chave de 10 bits e trabalha com blocos de dados de 8 bits para encriptação e decriptação.

## Estrutura do Projeto

Arquivos de Código:

- ```permutar.py```: Realiza permutações de bits conforme uma tabela especificada.

- ```deslocar_esquerda.py```: Executa deslocamento circular à esquerda nos bits.

- ```gerar_chaves.py```: Gera duas subchaves K1 e K2 a partir da chave principal.

- ```xor.py```: Executa a operação XOR bit a bit.

- ```caixa_s.py```: Aplica substituições não lineares usando as caixas S.

- ```funcao_fk.py```: Implementa a função Feistel.

- ```trocar.py```: Troca as metades esquerda e direita de um vetor de bits.

- ```encriptar.py```: Realiza a encriptação completa usando as subchaves.

- ```decriptar.py```: Realiza a decriptação invertendo o processo de encriptação.

- ```main.py```: Ponto de entrada principal para execução de testes.

## Como Executar

- Certifique-se de ter o Python instalado.

- Clone o repositório.

- Execute o arquivo ```main.py``` usando o comando: ```python main.py```

## Exemplo de Saída
```
Texto Original: [1, 1, 0, 1, 0, 1, 1, 1]

Texto Cifrado: [1, 0, 1, 0, 1, 0, 0, 0]

Texto Decriptado: [1, 1, 0, 1, 0, 1, 1, 1]
```
## Tecnologias Utilizadas

- Python 3.x
- PyCharm IDE

## Referências

- William Stallings - "Cryptography and Network Security"

- Documentações online sobre S-DES
