import random

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4] #para fazer listas usar colchetes
sort = random.choice(alunos)
print(f'O aluno que virá para o quadro é o {sort}!')

#Opção 2
from random import choice

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4] #para fazer listas usar colchetes
sort2 = choice(lista)
print(f'O aluno que virá para o quadro é o {sort2}!')
