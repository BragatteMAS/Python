# Desafio037_ Conversor de Bases Numéricas
#https://www.youtube.com/watch?v=B3F0IjH5WAM&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=38

from time import sleep
n = int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão:')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
c = int(input('Sua opção:'))
#print(f'Sua opção: {c}')
sleep(2)
if c == 1:
    bina = bin(n)[2:]
    print(f'{n} convertido em BINÁRIO é igual a \33[1:30:45m {bina} \33[m.')
elif c == 2:
    octa = oct(n)[2:]
    print(f'{n} convertido em OCTAL é igual a \33[1:30:44m {octa} \33[m.')
elif c == 3:
    hexa = hex(n)
    print(f'{n} convertido em HEXADECIMAL é igual a \33[1:30:42m {hexa[2:]} \33[m.')
else:
    print('Tu só poderias escolher entre 1 e 3, logo como diria o Faustão \33[1:30:41m "ERROUUU". \33[m')

#Opção do curso:
num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para a conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido em BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido em OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido em HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')
