#desafio045_GAME: Pedra Papel e Tesoura
#https://www.youtube.com/watch?v=tapTa6KVG-A&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=46
'''
from time import sleep
from random import shuffle

print(''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
'')
pedra = 0
papel = 1
tesoura = 2

lista = [pedra,papel,tesoura]
sort = shuffle(lista)

jogo = str(input("Qual é a sua jogada? "))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
if jogo == sort:
    print('EMPATOU')
elif jogo == pedra and sort == papel:
    print('Máquina venceu!')
elif jogo == pedra and sort == tesoura:
    print('Jogador venceu!')
#print('-='^40)
print(f''
Computador jogou {sort}
Jogador jogou {jogo}
{jogo} VENCE!
'')
#print('-='^40)
'''

#Solução cursoemvídeo:
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print(f'Computador escolheu {itens[computador]}')
print(f'Jogador escolheu {itens[jogador]}')
print('-=' * 11)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Empate')
    if jogador == 1:
        print('Jogador vence')
    if jogador == 2:
        print('Computador vence')
    else:
        print('Jogada inválida')
elif  computador == 1: #computador jogou papel
    if jogador == 0:
        print('Computador vence')
    if jogador == 1:
        print('Empate')
    if jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada inválida')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('Jogador vence')
    if jogador == 1:
        print('Computador vence')
    if jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')
