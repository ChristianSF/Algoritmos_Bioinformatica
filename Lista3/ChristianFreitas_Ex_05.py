#Christian Silva de Freitas
#RA: 140193

#5- Crie um vetor com 80 elementos igualmente espaçados
#entre 0 e 8π.

import numpy as np

if __name__ == '__main__':
  vetor = np.linspace(0, 8*np.pi, 80)
  print(vetor)
  print(vetor.size)