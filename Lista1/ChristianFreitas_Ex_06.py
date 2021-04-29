'''
6- Faça um programa chamado qtd_de_tinta.py que leia a
largura e a altura de uma parede em metros. Calcule a sua
área e a quantidade de tinta necessária para pinta-la. Sabe-
se que cada litro de tinta pinta uma área de 3 m2
'''

def qtd_de_tinta(a, l):
    area = a * l
    qtd = area / 3
    return qtd

# 1 = 3
# x = y

if __name__ == '__main__':
    a = float(input("Digite a altura da parede: "))
    l = float(input("Digite a largura da parede: "))

    print("A quantidade de tinta é: {} litros".format(qtd_de_tinta(a, l)))

