
"""
    Crie um programa chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

from d0111.utilidadescev import moeda

number = float(input("Digite o preço: R$"))
half_number = moeda.half(number)
double_number = moeda.double(number)
increase_ten = moeda.increase(number, 10)

print(f"A metade de R${number} é R${half_number}")
print(f"O dobro de R${number} é R${double_number}")
print(f"Aumentando 10%, temos R${increase_ten}")