
"""
    Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
    O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""

from time import sleep

from d0115.biblioteca.arquivo import *
from d0115.biblioteca.interface import *

file = "pessoas_cadastradas.txt"
if not file_exists(file):
    create_file(file)

while True:
    response = menu(["Listar pessoas cadastradas", "Cadastrar pessoas", "Sair"])
    if response == 1:
        read_file(file)
    elif response == 2:
        header("NOVO CADASTRO", "-")
        name = name_validation("Nome: ")
        age = read_integer("Idade: ")
        register(file, name, age)
    elif response == 3:
        header("Saindo do sistema... Ate logo!", "~")
        break
    else:
        print(f"{colors["red"]}ERRO: Digite uma opção válida!{colors["none"]}")
    sleep(2)
