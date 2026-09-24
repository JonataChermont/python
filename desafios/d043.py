
""" 
 Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
 calcule sei IMC e mostre seu status, de acordo com a tabela abaixo:
 - abaixo de 18.5: abaixo do peso
 - entre 18.5 e 25: peso ideal
 - 25 até 30: sobrepeso
 - 30 até 40: obesidade
 - acima de 40: obesidade mórbida
"""
print('ÍNDICE DE MASSA CORPORAL')

peso = float(input('Qual é o seu ? (Kg)'))
altura = float(input('Qual a sua altura ? (m)'))
imc = peso / (altura ** altura)
print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc <= 18.4:
    print('Voçê  está ABAIXO DO PESO')
elif imc >= 18.5 and imc <= 25:
    print('PARABÉNS! Voçê está no PESO IDEAL')
elif imc >= 26 and imc <= 30:
    print('Voçê está SOBREPESO')
elif imc >= 31 and imc <= 40:
    print('Voçê está em estado de OBESIDADE!')
elif imc > 41:
    print('Voçê está em estado de OBESIDADE MÓRBIDA!')
else:
    print('Voçê inseriu valores inválidos!')
