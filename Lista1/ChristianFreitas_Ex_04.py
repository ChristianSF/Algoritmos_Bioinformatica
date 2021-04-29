'''
Escreva um programa para calcular a redução do tempo de
vida de um fumante. Pergunte a quantidade de cigarros
fumados por dia e quantos anos ele já fumou. Considere que
um fumante perde 10 minutos de vida a cada cigarro e
calcule quantos dias de vida o fumante perderá. Exiba o
resultado em dias.
'''

def Calcula_Tempo(a, d):

    #Sabemos que um dia possui 1440 minutos
    total = a * 365 * d
    total = total
    total = total * 10
    total = total/1440

    return total

if __name__ == '__main__':
    d = int(input("Digite a quantidade de cigarros fumados por dia: "))
    a = int(input("Digite a quantidade de anos: "))

    print("Tempo de vida perdido: {:.1f} dias".format(Calcula_Tempo(a, d)))


