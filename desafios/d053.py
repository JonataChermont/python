
"""
    Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
    desconsidere os espaços.
    Ex: "APOS A SOPA
         A SACADA DA CASA
         A TORRE DA DERROTA
         O LOBO AMA O BOLO
         ANOTARAM A DATA DA MARATONA"
"""
print('DETECTOR DE PALÍNDROMO')

frase = input('Digite uma frase: ').strip().upper()
frase_limpa = frase.replace(' ', '')
inverso = ''

for i in range(len(frase_limpa) - 1, -1, -1):
    inverso += frase_limpa[i]

print(f'O inveso de {frase_limpa} é {inverso}')
if frase_limpa == inverso:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')
