#Ex1

"""
Desenvolva um programa que solicite o primeiro número
de uma PA e sua razão. O programa deve imprimir os 10
primeiros termos.
"""

def calcula_PA(r, n):
  print("O valor do termo 1 é de: {}".format(n))
  for i in range(9):
    n = n * r
    print("O valor do termo {} é de: {}".format(i+2, n))


if __name__ == '__main__':
  n = float(input("Digite o valor do primeiro termo: "))
  r = float(input("Digite o valor da razão: "))
  calcula_PA(r, n)