#Christian Silva de Freitas
#RA: 140193

# 2 Escreva uma função chamada maxnum que retorne o maior
# número de um conjunto de números. Utilize
# empacotamento para fazer a função.

def maxnum(lista):
    aux = 0
    for i in range(len(lista)):
        if aux < lista[i]:
            aux = lista[i]

    print("O maior elemento é: {}".format(aux))


if __name__ == '__main__':
    lista = []
    n = int(input("Digite a quantidade de elementos na lista: "))
    for i in range(n):
        elemento = int(input("Elemento N° {}: ".format(i + 1)))
        lista.append(elemento)

    maxnum(lista)