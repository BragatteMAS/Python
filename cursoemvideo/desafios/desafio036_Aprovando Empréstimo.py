v = float(input('Qual o valor da casa: R$ '))
s = float(input('Qual o salário do comprador: R$ '))
fi = int(input('Quantos anos de financiamento pretendido?' ))
d = v/(fi*12)
print( f' \33[35:40m Para pagar uma casa de {v} em {fi} anos a prestação será de {d}. \33[m')
if d >= (0.31 * s):
    print('\33[30:41m Lamento informar mas o empréstimo  foi \33[1m Negado! \33[1m')
else:
    print('Com sua renda o empréstimo foi  \33[1:30:46m concedido. \33[m')
