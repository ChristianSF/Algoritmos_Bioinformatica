#Christian Silva de Freitas
#RA: 140193

'''6- Escreva uma expressão que possa selecionar apenas os
elementos de índice par, de um array unidimencional,
independentemente do tamanho do vetor.
'''

if __name__ == '__main__':
  vetor = [9, 8, 7, 6, 5, 4, 3, 2, 1]
  novo = []

  for i in range(len(vetor)):
    if i % 2 == 0:
      novo.append(vetor[i])

  for i in range(len(novo)):
    print(novo[i])