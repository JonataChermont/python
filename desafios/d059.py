
"""
    Crie um programa que leia dois valores e mostre um menu
    como o abaixo:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso
"""
from time import sleep
print('CRIANDO UM MENU DE OPÇÕES')

primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
opcao = 0
maior = 0
while opcao != 5:
    print('''[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa''')
    opcao = int(input('>>>>> Digite sua opção: '))
    if opcao == 1:
        print(f'A soma entre {primeiro_valor} + {segundo_valor} é {primeiro_valor + segundo_valor}')
        print('=-='*15)
        sleep(2)
    elif opcao == 2:
        print(f'O resultado de {primeiro_valor} x {segundo_valor} é {primeiro_valor * segundo_valor}')
        print('=-='*15)
        sleep(2)
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            maior = primeiro_valor
        else:
            maior = segundo_valor
        print(f'Entre {primeiro_valor} e {segundo_valor} o maior valor é {maior}')
        print('=-='*15)
        sleep(2)
    elif opcao == 4:
        print('informe os números novamente:')
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))
        print('=-='*15)
        sleep(2)
    else:
        print('Opção inválida. Tente novamente.')
        sleep(2)
