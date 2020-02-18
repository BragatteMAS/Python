#desafio043_Índice de Massa Corporal
#https://www.youtube.com/watch?v=b7r34za963I&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=44

p = float(input('Qual o seu peso? (Kg) '))
a = float(input('Qual a sua altura? (m) '))
imc = p /(a ** 2)
print(f'O IMC desta pessoa é de {imc:.1f}')
if imc < 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc >= 24.9:
        print("Peso normal.")
elif imc >= 25 and imc >= 29.9:
        print("Sobrepeso.")
elif imc >= 30 and imc >= 34.9:
        print("Obesidade Grau 1.")
elif imc >= 25 and imc >= 29.9:
        print("Obesidade Grau 2.")
elif imc >= 40:
    print("Obesidade Grau 3. ")

#Solução cursoemvídeo:
peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
IMC = peso /(altura ** 2)
print(f'O IMC desta pessoa é de {IMC:.1f}')
if imc < 18.5:
    print("Você esta abaixo do peso normal.")
elif 18.5 <= imc < 2:
        print("Peso normal.")
elif 25 <= imc < 30:
        print("Você esta em Sobrepeso.")
elif 30 <= imc < 40:
        print("Você esta em Obesidade!")
elif imc >= 40:
    print("Você esta em Obesidade Mórbida, cuidado!")