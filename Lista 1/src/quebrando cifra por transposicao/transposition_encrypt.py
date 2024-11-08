# Elaborar o código para realizar a cifra por transposição (dica: pode escolher o metodo de permutação)

def transposition_encrypt(plaintext, key):
    num_columns = len(key)
    num_rows = (len(plaintext) + num_columns - 1) // num_columns
    plaintext = plaintext.ljust(num_columns * num_rows, 'X')

    matrix = [plaintext[i:i + num_columns] for i in range(0, len(plaintext), num_columns)]

    permuted_text = ''
    for col in sorted(range(num_columns), key=lambda x: key[x]):
        for row in matrix:
            permuted_text += row[col]

    return permuted_text
