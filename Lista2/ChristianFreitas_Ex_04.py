# Ex4

"""
Contar nucleotídeos de uma sequência de DNA. Podemos
pensar que uma fita de DNA - Genoma é simplesmente
uma string formada, somente, pelas letras 'A', 'C', 'G', 'T'.
Um exemplo seria a seguinte string:
"ATGCTTCAGAAAGGTCTT.".

a. verificar se a sequência de DNA digitada pelo
usuário é válida. caso o usuário digite letras
diferentes de ATCG o código deve informar:
“sequência de DNA invalida”. Caso a sequência
digitada foi valida o programa deve:
b. imprimir o número total de nucleotídeos na
sequência
c. Calcular e imprimir a quantidade de cada um dos
quartos nucleotídeos
d. calcular e imprimir a frequência (%) de cada um dos
nucleotídeos
"""

def Funcao(sequencia):
    adenina = 0
    citosina = 0
    guanina = 0
    citosina = 0
    timina = 0
    sequencia = sequencia.upper()

    if (len(sequencia) % 2) > 0:
        print("Sequência inválida")
    else:

        for i in range(len(sequencia)):
            if sequencia[i] == 'A':
                adenina += 1
            elif sequencia[i] == 'C':
                citosina += 1
            elif sequencia[i] == 'T':
                timina += 1
            elif sequencia[i] == 'G':
                guanina += 1
            else:
                print("Sequência inválida")
                break

        print("Sequência válida\n")

        print("O número de nucleotídeos na sequência é: ", len(sequencia))
        print("\nA sequência possui: ")
        print("Número de Adeninas: ", adenina)
        print("Número de Citosinas: ", citosina)
        print("Número de timinas: ", timina)
        print("Número de Guanina: ", guanina)
        print("\nA frequência de nucleotídeos na sequência é: ")
        f_A = (adenina * 100) / len(sequencia)
        print("{:.2f}% Adeninas (A)".format(f_A))
        f_G = (guanina * 100) / len(sequencia)
        print("{:.2f}% Guanina (A)".format(f_G))
        f_C = (citosina * 100) / len(sequencia)
        print("{:.2f}%  Citosina (C)".format(f_C))
        f_T = (timina * 100) / len(sequencia)
        print("{:.2f}% Timinia (T)".format(f_T))

if __name__ == '__main__':
    sequencia = input("Digite a sequencia: ")
    Funcao(sequencia)