#Solução Bragatte
n = str(input('Digite seu nome completo: ')).strip().split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {n[0]}.')
#print(f'Seu último nome é {n[3]}.')
print(f'Seu último nome é {(n[len(n)-1])}.') #solução otimizada | ao referenciar ação para valor colocar colchetes

# Solução Curso
#n = str(input('Digite seu nome completo: ')).strip()
#ome = n.split()
#print('Muito prazer em te conhecer!')
#print(f'Seu primeiro nome é {nome[0]}.')
#print('Seu último nome é {}.'.format(nome[len(nome)-1]))

