

print('PINTANDO PAREDES')

largura_parede = float(input('Largura da parede: '))
altura_parede = float(input('Altura da parede: '))

area = altura_parede * largura_parede
quantidade_tinta = area / 2

print(f'Sua parede tem a dimensão de {largura_parede} x {altura_parede} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, voçê precisará de {quantidade_tinta:.2f}L de tinta')
