# -*- coding: utf-8 -*-
"""Algoritmo_SmithWaterman

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mVLFN6Y6TTz6VnN3RLN8Ep3-pA4_6JLl
"""

import numpy as np

match = 1
mismatch = -1
gap = -2

def algoritmo_sw():

  for i in range(0,len(sequencia1)+1):
      for j in range(0,len(sequencia2)+1):
        if matriz_principal[i][j] < 0:
          matriz_principal[i][j] = 0

  print(matriz_principal)
  print("\n")

def cria_matriz(sequencia1, sequencia2):
  for i in range(len(sequencia1)):
      for j in range(len(sequencia2)):
          if sequencia1[i] == sequencia2[j]:
              matriz_match[i][j]= match
          else:
              matriz_match[i][j]= mismatch

  print("\n")
  print(matriz_match)
  print("\n")

  for i in range(len(sequencia1)+1):
      matriz_principal[i][0] = i*gap
  for j in range(len(sequencia2)+1):
      matriz_principal[0][j] = j * gap

  for i in range(1,len(sequencia1)+1):
      for j in range(1,len(sequencia2)+1):
          matriz_principal[i][j] = max(matriz_principal[i-1][j-1]+matriz_match[i-1][j-1],
                                  matriz_principal[i-1][j]+gap,
                                  matriz_principal[i][j-1]+ gap)

  print(matriz_principal)
  print("\n")

def alinha_sequencia(sequencia1, sequencia2):

  alinhamento_1 = ""
  alinhamento_2 = ""

  ti = len(sequencia1)
  tj = len(sequencia2)

  algoritmo_sw()

  while (ti > 0 and tj > 0):

    if (ti >0 and tj > 0 and matriz_principal[ti][tj] == matriz_principal[ti-1][tj-1]+ matriz_match[ti-1][tj-1]):

      alinhamento_1 = sequencia1[ti-1] + alinhamento_1
      alinhamento_2 = sequencia2[tj-1] + alinhamento_2

      ti = ti - 1
      tj = tj - 1
      
    elif (ti > 0 and matriz_principal[ti][tj] == matriz_principal[ti-1][tj] + gap):
      alinhamento_1 = sequencia1[ti-1] + alinhamento_1
      alinhamento_2 = "-" + alinhamento_2

      ti = ti -1
    else:
      alinhamento_1 = "-" + alinhamento_1
      alinhamento_2 = sequencia2[tj-1] + alinhamento_2

      tj = tj - 1

  print(alinhamento_1)
  print(alinhamento_2)


if __name__ == '__main__':

  sequencia1 = input("Digite a sequ??ncia 1: ")
  sequencia2 = input("Digite a sequ??ncia 2: ")

  sequencia1 = sequencia1.upper()
  sequencia2 = sequencia2.upper() 

  print("\n")

  matriz_principal = np.zeros((len(sequencia1)+1,len(sequencia2)+1))
  matriz_match = np.zeros((len(sequencia1),len(sequencia2)))

  print(matriz_principal)

  cria_matriz(sequencia1, sequencia2)
  alinha_sequencia(sequencia1, sequencia2)
