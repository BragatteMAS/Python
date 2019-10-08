#opção Bragatte
#f = str(input('Digite uma frase: ')).strip()
#a = f.count("a")
#A = f.count("A")
#r = a + A
#print(f'A letra A aparece {r} na frase.')
#fA = f.upper() # colocou todos os caracteres no formato maiúsculo, facilitar a busca
#print(f'A primeira letra A aparece na posição {fA.find("A")+1}.')
#print(f'A última letra A aparece na posição {fA.rfind("A")+1}.')

#opção curso
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra A aparece na posição {frase.find("A")+1}.')
print(f'A última letra A aparece na posição {frase.rfind("A")+1}.')
