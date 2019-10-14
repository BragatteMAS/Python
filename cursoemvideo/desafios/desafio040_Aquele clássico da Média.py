#desafio040_Aquele clássico da Média
#https://www.youtube.com/watch?v=QuWDyUeoaJs&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=41

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
print(f'Tirando {n1:.2f} e {n2:.2f}, a média do aluno é {m:.2f}.')
if m >= 7.00:
    print('O aluno(a) está APROVADO.')
elif m >=5.0 and m <= 6.9:
    print('O aluno(a) está de RECUPERAÇÃO.')
else:
    print('O aluno(a) está de REPROVADO')
