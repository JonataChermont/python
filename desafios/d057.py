
"""
    Faça um programa que leia o sexo de uma pessoa,
    mas só aceite os valores 'M' ou 'F'. Caso esteja.
    Caso esteja errado, peça a digitação novamente
    até ter um valor correto.
"""
print('VALIDAÇÃO DE DADOS')

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
    
if sexo == 'M':
    print('Sexo masculino registrado')
else:
    print('Sexo feminino registrado')