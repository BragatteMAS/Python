n = str(input('Qual é seu nome completo? ')).strip()
sep = n.split()
sobre = 'Silva'
print(f'Seu nome tem Silva? {sobre in sep}')
