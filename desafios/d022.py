

print('ANALISADOR DE TEXTOS')

nome = input('Digite seu nome completo: ').strip()
primeiro_nome = nome.split()
numero_letras_nome = nome.replace(' ', '')
print('Analisando seu nome...')

print(f'Seu nome em maiúsculas é {nome.upper().strip()}')
print(f'Seu nome em minúsculas é {nome.lower().strip()}')
print(f'Seu nome tem ao todo {len(numero_letras_nome)} letras')
print(f'Seu primeiro nome é {primeiro_nome[0]} e ele tem {len(primeiro_nome[0])} letras')
