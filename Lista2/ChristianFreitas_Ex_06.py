#6
"""
A partir da leitura do arquivo Corona_genomic.fasta,
Calcule a fita complementar e salve a resposta em
um arquivo chamado ex06_a.txt
"""

#!pip install biopython
#!pip install pandas
#!pip install numpy

from Bio.Seq import Seq
import pandas as pd
import numpy as np

#--------------- Primeira Parte ---------------

arquivo = 'Corona_genomic.fasta';

p = open(arquivo, 'r')
linhas = p.readlines()

lista = []

for i in linhas:
    if i.find('>') != 0:
        lista.append(i)

n = 1
for i in range(len(lista)):
  lista[i] = lista[i].replace("\n", "")


#--------------- Segunda Parte ---------------

lista_complementar = []

for i in range(len(lista)):
  sequencia = Seq(lista[i])
  lista_complementar.append(str(sequencia.complement))

for i in range(len(lista_complementar)):
  lista_complementar[i] = lista_complementar[i].replace("<bound method Seq.complement of Seq('", "")
  lista_complementar[i] = lista_complementar[i].replace("')>", "")
  #print(lista_complementar[i])

dados = pd.DataFrame(lista_complementar, columns=["Fita"])
#dados.head()
np.savetxt(r'ex06.txt', dados.values, fmt='%s', delimiter='\t')