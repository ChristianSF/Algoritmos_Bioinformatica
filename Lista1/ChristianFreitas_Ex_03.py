'''
Escreva um programa que faça a conversão da temperatura
de graus celsius para Fahrenheit.
'''

def conversao(temperatura_c):

  temp_final = (160+(9*temperatura_c))/5
  return temp_final

if __name__ == '__main__':
    valor = float(input("Digite o valor quer deseja converter: "))
    print("O temperatura em °F é:", conversao(valor))