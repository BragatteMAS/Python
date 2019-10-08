from datetime import date

print('\33[7m Be commited to change!')
ano = int(input('\33[7m Que ano quer analisar? \33[7:33m Coloque 0 para analisar o ano atual: \33[m'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #divisíveis por 4 e 400 (igual==0) e não podem por 100(nãoigual!=0)
    print(f'O ano {ano} é \33[7:36m BISSEXTO.\33[m')
else:
    print(f'O ano {ano} NÃO é \33[7:31m BISSEXTO.\33[m')
