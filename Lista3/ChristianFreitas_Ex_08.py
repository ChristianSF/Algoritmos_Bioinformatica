#Christian Silva de Freitas
#RA: 140193

'''8) Crie um vetor x com 150 pontos linearmente espaçados
entre -2π e 2π e construa o gráfico a baixo. Utilize as
bibliotecas numpy e matplotlib
'''

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
  x = np.linspace(-2*np.pi, 2*np.pi, 150)
  seno = np.sin(x)
  cosseno = np.cos(x)
  tangente = np.tan(x)

  #print(tangente)
  fig, ax = plt.subplots(2,2, figsize=(14,6))
  ax[0,0].plot(x, seno)
  ax[0,0].set_title('Função Seno')
  ax[0,0].set(xlabel='Valor de X', ylabel='Valor de Y')
  ax[0,1].plot(x, cosseno,  'P')
  ax[0,1].set_title('Função Cosseno')
  ax[0,1].set(xlabel='Valor de X', ylabel='Valor de Y')
  ax[1,0].plot(x, tangente, 'o')
  ax[1,0].set_title('Função Tangente')
  ax[1,0].set(xlabel='Valor de X', ylabel='Valor de Y')