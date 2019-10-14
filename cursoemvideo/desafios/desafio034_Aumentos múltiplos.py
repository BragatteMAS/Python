#Desafio034 Aumentos Múltiplos
salario = float(input('Qual é o salaŕio do funcionário? R$ '))
A10 = (salario * 10) / 100
A15 = (salario * 15) / 100
Aumento10 = salario + A10
Aumento15 = salario + A15
if salario >= 1250:
    print(f' \33[1:31:40m Quem ganhava R${salario} passa a ganhar R${Aumento10} agora. \33[m')
else:
    print(f' \33[1:36:40m Quem ganhava R${salario} passa a ganhar R${Aumento15} agora \33[m')

#Solução Curso
salário = float(input('Qual é o salaŕio do funcionário? R$ '))
if salario <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salário,novo))

