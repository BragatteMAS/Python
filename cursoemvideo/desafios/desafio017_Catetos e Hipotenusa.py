
co = float(input('digite o comprimento do cateto oposto do triangulo retangulo: '))
ca = float(input('digite o comprimento do cateto adjacante: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa do triângulo retângulo é {h:.2f}.')

x = float(input('digite o comprimento do cateto oposto do triangulo retangulo: '))
y = float(input('digite o comprimento do cateto adjacante: '))
from math import hypot
print(hypot(x,y))
#or
import math
hi = math.hypot(x, y)
print(hi)
