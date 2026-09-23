
# escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite
print('RADAR ELETRÔNICO')

velocidade_carro = int(input('Qual é a velocidade do carro ? '))
limite_velocidade = 80
multa_por_km = 7
valor_multa = (velocidade_carro - limite_velocidade) * multa_por_km

if velocidade_carro > limite_velocidade:
  print(f'MULTADO! Voçê excedeu o limite permitido que é de {limite_velocidade}Km/h')
  print(f'Voçê deve pagar uma multa de R${valor_multa}!')
print('Tenha um bom dia! Diriga com segurança!')
