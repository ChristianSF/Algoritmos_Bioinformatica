#Christian Silva de Freitas
#RA: 140193

'''7- Crie uma matriz 4 x 5 de números aleatórios inteiros no
intervalo -10 a 65 e armazene em uma variável “matrix”.
a. Escreva um comando que retorna o valor absoluto dos
elementos dessa matriz.
b. Escreva um comando que retorna o seno dos valores
contidos na primeira linha dessa matriz.
c. Escreva um comando que retorne o valor máximo das
colunas da matriz
d. Calcule a soma dos elementos em cada coluna da
matriz
e. Calcule a soma dos elementos em cada linha da matriz
f. Calcule o produto entre os elementos de cada coluna
da matriz. Dica: procure no google como resolver isso
'''

import numpy as np

if __name__ == '__main__':
    matrix = np.random.randint(-10, 65, size=(4, 5))

    # A - Valor Absoluto
    print("Valores Absolutos: ")
    for i in range(4):
        for j in range(5):
            print("{} ".format(np.abs(matrix[i][j])))
    print("\n")
    # B- Retornar Seno
    i = 0
    print("Seno da primeira linha: ")
    for j in range(5):
        print(np.sin(matrix[i][j]))

    print("\n")
    # C- Valor máximo
    print("Valor máximo de cada coluna:")
    matrix_nova = np.transpose(matrix)
    # for i in range(5):
    # for j in range(4):
    # print(matrix_nova[i][j])
    print(matrix_nova[0].max())
    print(matrix_nova[1].max())
    print(matrix_nova[2].max())
    print(matrix_nova[3].max())
    print(matrix_nova[4].max())

    # D- Soma total da coluna
    print("\n")
    print("Soma de cada coluna:")
    for i in range(len(matrix_nova)):
        print(matrix_nova[i].sum())

    # E- Soma total da linha
    print("\n")
    print("Soma de cada linha:")
    for i in range(len(matrix)):
        print(matrix[i].sum())

    # F- Produto de cada coluna
    a = 1
    print("\n")
    print("Produto de cada coluna: ")
    for i in range(len(matrix_nova)):
        for j in range(len(matrix)):
            a *= matrix_nova[i][j]
        print(a)
