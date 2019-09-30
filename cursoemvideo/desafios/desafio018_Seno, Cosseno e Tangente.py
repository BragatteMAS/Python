import math

ang = int(input('Digite o ângulo de interesse: '))

# Opção 1
conv = math.radians(ang)
sen = math.sin(conv)
cos = math.cos(conv)
tan = math.tan(conv)
print(
    f'Os valores referentes ao ângulo {ang} para seno, cosseno e tangente na opção 1 são respectivamente {sen:.2f},{cos:.2f} e {tan:.2f}.')

from math import radians, sin, cos, tan

# Opção 2 - mais curta no código
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(
    f'Os valores referentes ao ângulo {ang} para seno, cosseno e tangente na opção 2 são respectivamente {seno:.2f},{cosseno:.2f} e {tangente:.2f}.')
