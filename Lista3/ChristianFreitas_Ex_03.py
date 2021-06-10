#Christian Silva de Freitas
#RA: 140193

#3 Escreva uma função que receba dois números e retorne
#True se o primeiro número for múltiplo do segundo.

def funcao(a, b):
  if b % a == 0:
    print("True")
  else:
    print("False")

if __name__ == '__main__':
  a = int(input("Digite o primeiro número: "))
  b = int(input("Digite o segundo número: "))
  funcao(a, b)