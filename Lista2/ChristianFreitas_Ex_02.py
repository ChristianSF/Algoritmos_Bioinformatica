#Ex2

"""
Escreva um programa que pergunte o deposito inicial e a
taxa de Juros de uma poupança. Exiba os valores mês a
mês para os 24 primeiros meses. No final deve imprimir o
total de ganho com juros no período.
"""

def Calcula_Juros(inicio, juros):
  total = inicio * juros * 24
  return total


if __name__ == '__main__':
  inicio = float(input("Digite o depósito inicial: "))
  juros = float(input("Digite a taxa de juros: "))
  print("O total é: R${}".format(inicio + Calcula_Juros(inicio, juros)))
  print("O total ganho em juros é: R${}".format(Calcula_Juros(inicio, juros)))