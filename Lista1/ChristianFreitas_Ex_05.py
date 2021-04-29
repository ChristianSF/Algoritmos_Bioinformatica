'''
5- Escreva um programa que leia a quantidade de dias, horas,
minutos e segundos. Calcule o total em segundos.
'''

def Converte_Segundos(d, h, m, s):
    ''' Sabemos que:
        1 minuto tem: 60 segundos
        1 hora tem:  3600
        1 dia tem: 86400 segundos
    '''
    if(d == 0):
        dia_s = 0
    else:
        dia_s = d * 86400

    if (h == 0):
        hora_s = 0
    else:
        hora_s = h * 3600

    if(m == 0):
        minutos_s = 0

    else:
        minutos_s = m * 60

    total = dia_s + hora_s + minutos_s + s
    return total

if __name__ == '__main__':
    d = int(input("Digite a quantidade de Dias: "))
    h = int(input("Digite a quantidade de Horas: "))
    m = int(input("Digite a quantidade de Minutos: "))
    s = int(input("Digite a quantidade de Segundos: "))

    print("O total é: {} segundos".format(Converte_Segundos(d, h, m, s)))