
"""
    Faça um programa que tenha uma função chada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""

print(f"{"-" * 19}\nCONTROLE DE TERRENO\n{"-" * 19}")

def area(largura, comprimento):
    area = largura * comprimento
    print(f"A área de um terreno {largura:.1f}x{comprimento:.1f} é de {area:.1f}m².")

def validacao_dados(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print("Valor inválido!")

area(
    validacao_dados("LARGURA (m): "),
    validacao_dados("COMPRIMENTO (m): ")
)
