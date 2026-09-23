
#crie programa que leia o nome de um cidade e diga
#se ela começa ou não com o nome "santo".
print('VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO')

cidade = input('Em que cidade voçê nasceu ? ').strip().lower()
primeiro_nome_cidade = cidade.split()
print('santo' in primeiro_nome_cidade[0])

