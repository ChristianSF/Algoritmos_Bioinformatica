#Ex5
"""
crie um código em python na qual faça a leitura do
arquivo fasta chamado Corona_genomic.fasta e imprima
somente a sequencia de aminoácidos.
"""

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
  print("Linha {}- {}".format(i, lista[i]))
  n += 1

print("\nNúmero de linhas: ", i)