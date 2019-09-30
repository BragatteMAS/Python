num = float(input('Digite um número:'))
numi = int(num)
print(f'O número digitado {num} tem a parte inteira {numi}.')

from math import sqrt
import math
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {raiz:.3f}, arredondada para cima fica {math.ceil(raiz)} e arredondada para baixo fica {math.floor(raiz)}.')
