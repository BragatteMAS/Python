algo = input('Digite algo: ') #função input sempre retorna tipo primitivo Str!!!
print('Qual é o Tipo primitivo desse valor:', type(algo))
print('É composto por números?', algo.isnumeric())
print('É composta por letras/alfabético? ', algo.isalpha())
print('É composto por alfanúmericos? ', algo.isalnum())
print('É composto somente por letras maiúsculas? ', algo.isupper())
print('É composto somente por letras minúsculas? ', algo.islower())
print('É composto por somente espaços? ', algo.isspace())
print('É capitalizada? ', algo.istitle())#Possui uma letra maiúscula
