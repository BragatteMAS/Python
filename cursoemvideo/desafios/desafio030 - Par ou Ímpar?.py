import numpy as np
n = int(input('\033[35m Me diga um número qualquer: \033[m'))
r = n % 2 #O resto da divisão de qualquer número par por dois é zero e qualquer ímpar é um.
#print(f'\033[36:40m O resultado foi {r}.\033[m')
if r == 0:
    print(f'O número {n} é \033[1:34:40m PAR \033[m')
else:
    print(f'O número {n} é \033[1:31:40m ÍMPAR \033[m')
