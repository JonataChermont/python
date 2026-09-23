
# desenvolva um programa que pergunte a distância de uma viagem
# em km. Calcule o preço da passagem, cobrando R$0,50 por km para
# viagens de até 200km e R$0,45 para viagens mais longas
print('CUSTO DA VIAGEM')

distancia_viagem = int(input('Qual é a distância da sua viagem ? '))
preco_200km = 0.50
preco_mais_de_200km = 0.45

print(f'Voçê está prestes a começar uma viagem de {distancia_viagem}Km.')
if distancia_viagem <= 200:
  print(f'E o preço da sua passagem será de R${preco_200km * distancia_viagem:.2f}')
else:
  print(f'E o preço da sua passagem será de R${preco_mais_de_200km * distancia_viagem:.2f}')