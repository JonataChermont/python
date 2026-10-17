
"""
    Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
    ex:
    escreva("Olá, mundo!")
    saída:
    -------------------
        Olá, mundo!
    -------------------
"""

def escreva(texto):
    tamanho_texto = len(texto) * 2
    if len(texto) % 2 == 1:
        print(f"{"-" * (tamanho_texto - 1)}\n{texto.center(tamanho_texto)}\n{"-" * (tamanho_texto - 1)}")    
    else:
        print(f"{"-" * tamanho_texto}\n{texto.center(tamanho_texto)}\n{"-" * tamanho_texto}")

escreva("UM PRINT ESPECIAL")     
escreva(str(input("Digite alguma coisa: ")))
