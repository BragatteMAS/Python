d = float(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos km o carro percorreu?'))
p = (60 * d) + (km * 0.15)
print(f'O total a pagar é de R$ {p:.2f}.')
