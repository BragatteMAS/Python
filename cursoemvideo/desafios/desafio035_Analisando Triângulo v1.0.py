print('\033[30:42m-=-=\033[m' * 20)
print(' \033[7:30:42m Analisador de triângulos \033[m')
print('\033[30:42m-=-=\033[m' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1< r2 + r3 and r2 < r1 + r3 and r2< r1 + r2:
    print('Os segmentos acima \033[1:34m PODEM FORMAR \033[m um triângulo. \033[m')
else:
    print('Os segmentos acima \033[1:31m NÃO PODEM FORMAR \033[m um triângulo. \033[m')
