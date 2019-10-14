#Desafio038_Comparando números
#https://www.youtube.com/watch?v=iuPbB9uHczM&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=39

n1 = input('Primeiro número: ')
n2 = input('Segundo número: ')

if n1 == n2:
    print('Os valores são iguais!')
elif n1 >= n2:
    print('O Primeiro valor é maior!')
elif n1 <= n2:
    print('O Segundo valor é maior!')

#Opção do curso:
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior!')
elif n2 > n1:
    print('O SEGUNDO valor é maior!')
else:
    print('Os valores são IGUAIS!')
