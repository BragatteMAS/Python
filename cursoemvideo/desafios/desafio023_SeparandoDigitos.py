n = int(input('Informe seu número: '))
print(f'Analisando o número {n}.')
#Opção1
#ns = str(n)
#print(f'Unidade: {ns[3]}')
#print(f'Dezena: {ns[2]}')
#print(f'Centena: {ns[1]}')
#print(f'Milhar: {ns[0]}')

#Opção 2
u = n //1 % 10
d = n //10 % 10
c = n //100 % 10
m = n //1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
