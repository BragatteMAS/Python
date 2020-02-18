#desafio044_Gerenciador de Pagamentos
#https://www.youtube.com/watch?v=I-SH3QchuZ4&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=45

name = 'Bragatte Tech'
print(f'{name:=^40}')

preço = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opção = int(input('Sua opção: '))
if opção == 1:
    desconto = preço - (preço * 10 / 100)
    print(f'Sua compra de R${preço:.2f} vai custar R${desconto:.2f} no final.')
elif opção == 2:  
    desconto = preço - (preço * 5 / 100)
    print(f'Sua compra de R${preço:.2f} vai custar R${desconto:.2f} no final.')
elif opção ==3:
    vezes = preço / 2
    print(f'Sua compra de R${preço:.2f} terá duas parcelas de R${vezes:.2f}, sem juros.')
elif opção == 4:
    parcela = int(input('Quantas parcelas? '))
    juro = (preço * 0.2)
    valor = (juro+preço) / parcela
    print(f'Sua compra será parcelada em {parcela}x de R${valor:.2f} com JUROS.')
    print(f'Sua compra de R${preço:.2f} vai custar R${(juro+preço):.2f} no final.')
else:
    print('Método de pagamento inválido. Optar por uma das opções disponíveis para efetuar a compra.')


#Solução cursoemvídeo:
print('{:=^40}'.format('LOJA GUANABARA'))

preço = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a sua opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:  
    total = preço - (preço * 5 / 100)
elif opção ==3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcelas = total / totparc
    print('Sua compra será parcelada em R${}x de R${:.2f} COM JUROS.'.format(totparc, parcelas))
else:
    total = 0
    print('OPÇÃO  INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,total))