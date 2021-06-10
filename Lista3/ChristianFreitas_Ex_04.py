#Christian Silva de Freitas
#RA: 140193

'''4 Crie um programa que leia nome, sexo, peso e altura de
várias pessoas. guarde os dados de cada pessoa num
dicionário individual e acrescente o IMC da pessoa. Organize
todos os dicionários em uma lista. No final mostre
a. Quantas pessoas foram cadastradas
b. Qual é o peso médio das pessoas
c. Qual é a altura média das pessoas
d. Qual é IMC médio das pessoas
'''

#Não terminei esse exercicio 

import numpy as np

def funcao(pessoas):
  for k, v in pessoas.items():
    print("teste")


if __name__ == '__main__':
  pessoas = []
  n = int(input("Digite a quantidade de pessoas que quer cadastrar: "))
  for i in range(n):
    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo: ")
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    imc = peso/(altura**2)
    pessoas.append({'nome':nome, 'sexo':sexo, 'peso':peso, 'altura':altura, 'imc':imc})

  funcao(pessoas)