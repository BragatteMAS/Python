#desafio033_Maior ou menor
n1 = int(input('\33[37m Primeiro valor: \33[m'))
n2 = int(input('\33[32m Segundo valor: \33[m'))
n3 = int(input('\33[31m Terceiro valor: \33[m'))
lista = [n1,n2,n3]
menor = min(lista)
maior = max(lista)
print(f'O menor valor digitado foi\33[7:34:40m {menor}.\33[m')
print(f'O maior valor digitado foi\33[7:35:40m {maior}.\33[m')

#Opção do curso
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#verificando quem é o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
