

print('DISSECANDO VARIÁVEIS')

texto = input('Digite algo: ')
print(f'o tipo primitivo desse valor é {type(texto)}') #tipo
print(f'só tem espaço ? {texto.isspace()}') #espaço
print(f'é um número ? {texto.isnumeric()}') #numero
print(f'é alfabético ? {texto.isalpha()}') #alfabetico
print(f'é alfanumerico ? {texto.isalnum()}') #alfanumerico
print(f'está em maiúsculas ? {texto.isupper()}') #maiuscula
print(f'está em minúsculas ? {texto.islower()}') #minuscula
print(f'está capitalizada ? {texto.istitle()}') #capitalizada


