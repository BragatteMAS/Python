#Desafio028 Jogo da Adivinhação v.1.0
from numpy import random
from time import sleep
print('\033[36m * \033[m' * 20)
print(' \033[7:34:40m Vou pensar em um número entre 0 e 5. Tente adivinhar... \033[m')
print('\033[36m * \033[m' * 20)
c = random.randint(0,5) #número sorteado pelo computador
j = int(input('Em que número eu pensei?')) #Chute jogador.
print('\033[1:35m Processando...\033[m')
sleep(1) #temporizador para dar tensão
if c == j:
    print(f'\033[33m Parabéns você ganhou, pois pensou no valor {j} e eu também. Está convidado para sair da Matrix! \033[m')
else:
    print(f'\033[31m Suas chances eram de seis para um, você ficou dentro da estatística e não acertou pensando em {j}. O número era {c}. \033[m')
