

#faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra "a"
#em que posição ela aparece a primeira vezes
#em que posição ela aparece a última vez
print('PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING')

frase = input('Digite uma frase: ').strip().lower()
print(f'A letra "A" aparece {frase.count('a')} vezes ')
print(f'A primeira letra "A" apareceu na posição {frase.find('a') + 1}')
print(f'A última letra "A" apareceu na posição {frase.rfind('a') + 1}')

