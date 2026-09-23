

print('ALUGUEL DE CARROS')

dias = int(input('Quantos dias alugados ? '))
kilometros = float(input('Quantos km rodados ? '))

pago = (dias * 60) + (kilometros * 0.15)

print(f'O total a ser pago é de R${pago:.2f}')
