# desafio041_Classificando atletas
# https://www.youtube.com/watch?v=ZiC5NgSGJXU&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=8

from datetime import date

atual = date.today().year
ano = int(input('Qual ano de nascimento do atleta?'))
idade = atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('O atleta é da classe MIRIM!')
elif idade <= 14:
    print('O atleta é da classe INFANTIL!')
elif idade <= 19:
    print('O atleta é da classe JUNIOR!')
elif idade <= 25:
    print('O atleta é da classe SENIOR!')
else:
    print('O atleta é da classe MASTER!')

#Solução cursoemvídeo:
#from datetime import date
#atual = date.today().year
#nascimento = int(input('Ano de Nascimento: '))
#idade = atual - nascimento
#print('O atleta tem {} anos.'.format(idade)
#if idade <= 9:
#    print('Classificação: MIRIM')
#if idade <= 14:
#    print('O atleta é da classe INFANTIL!')
#elif idade <= 19:
#    print('O atleta é da classe JUNIOR!')
#elif idade <= 25:
#    print('O atleta é da classe SENIOR!')
#else:
#    print('O atleta é da classe MASTER!')
