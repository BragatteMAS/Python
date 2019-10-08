#desafio031 - Custo da viagem
custo = float(input('\33[1:34:40m Qual a distância em km da sua viagem ?\33[m'))
print(f'\33[1:32m Você esta prestes a começar uma viagem de \33[4m {custo}km.\33[m')
perto = custo * 0.50
longe = custo * 0.45
if custo <= 200:
    print(f'\33[m E o preço da sua passagem será de \33[32m R$ {perto:.2f} \33[m.')
else:
    print(f'\33[m E o preço da sua passagem será de \33[7:31:40m R$ {longe:.2f} \33[m.')

#Opção Curso
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km,'.format(distância))
preço = distância *0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(preço))
