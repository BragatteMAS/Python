#desafio039_Alistamento Militar.py
#https://www.youtube.com/watch?v=ePwP4gU_waY&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=40
from datetime import date
year = date.today().year
born = int(input('Ano de nascimento: '))
age = year - born
gen = str(input('Você é do gênero masculino ou feminino?'))
if gen == 'feminino':
    print('O alistamento para você é facultativo.')
elif gen == 'masculino':
    print('Siga as orientações.')
else:
    print('Por gentileza preencha com seu gênero, conforme orientado!')
    gen = str(input('Você é do gênero masculino ou feminino?'))
###
if age == 1:
    print(f'Quem nasceu em {born} tem ou fará {age} ano em {year}.')
elif age < 0:
    print(f'Você ainda não nasceu criatura. Como esta respondendo isso!!!!')
else:
    print(f'Quem nasceu em {born} tem {age} anos em {year}.')
##
if age < 18 and gen != 'feminino':
    alist = 18 - age
    print(f'Ainda faltam {alist} anos para o alistamento.')
    d_alist = year + alist
    print(f'Seu alistamento será em {d_alist}.')
elif age == 18 and gen != 'feminino':
    print(f'Você tem que se alistar IMEDIATAMENTE!')
elif age > 18 and gen != 'feminino':
    alist = age - 18
    print(f'Você já deveria ter se alistado há {alist} anos')
    d_alist = year - alist
    print(f'Seu alistamento foi em {d_alist}.')
##
#Opção do curso:
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
