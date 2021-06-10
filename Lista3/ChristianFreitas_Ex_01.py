#Christian Silva de Freitas
#RA: 140193

#1 Escreva uma função chamada fatorial para calcular o
#fatorial de um número inteiro.

def fatorial(fat):
  if fat == 0:
    return 0
  elif fat == 1:
    return 1
  else:
    return fatorial(fat - 1) * fat


if __name__ == '__main__':
  a = int(input("Digite o número que deseja calcular o fatorial: "))
  print("O fatorial de {} é: {}".format(a, fatorial(a)))