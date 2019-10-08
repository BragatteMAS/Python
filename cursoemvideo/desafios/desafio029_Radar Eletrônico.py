#Desafio029 - Radar Eletrônico
v = int(input('Qual a velocidade atual do carro em km? '))
if v <= 80:
    print('\033[32m Tenha um bom dia! Dirija com cuidado.\033[m')
else:
    print('\033[1:31m MULTADO! \033[0:31m Você excedeu o limite permitido que é de 80km/h.\033[m')
    multa = (v - 80) * 7
    print(f'\033[33m Você deve pagar uma multa de \033[1:31:40m R${multa}!\033[m')
    print('\033[1:32m Tenha um bom dia! Dirija com cuidado.\033[m')
