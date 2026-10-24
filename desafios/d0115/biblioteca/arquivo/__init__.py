
from d0115.biblioteca.interface import colors, header

path = "/home/jonata/Documentos/estudos/python/desafios/d0115/"

def file_exists(name):
    try:
        file = open(f"{path}{name}", "rt")  # noqa: SIM115
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True

def create_file(name):
    try:
        file = open(f"{path}{name}", "wt+")  # noqa: SIM115
        file.close()
    except:  # noqa: E722
        print(f"{colors["red"]}Ouve um erro na criação do arquivo{colors["none"]}")
    else:
        print(f"Arquivo {name} ciado com sucesso")

def read_file(name):
    try:
        file = open(f"{path}{name}", "rt")  # noqa: SIM115
    except:  # noqa: E722
        print(f"{colors["red"]}ERRO ao ler o arquivo!{colors["none"]}")
    else:
        header("PESSOAS CADASTRADAS", "-")
        for linha in file:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<35}{dado[1]:>2} anos")
    finally:
        file.close()

def register(file, name="desconhecido", age=0):
    try:
        archive = open(f"{path}{file}", "at")  # noqa: SIM115
    except:  # noqa: E722
        print(f"{colors["red"]}Houve um ERRO ao abrir o arquivo!{colors["none"]}")
    else:
        try:
            archive.write(f"{name};{age}\n")
        except:  # noqa: E722
            print(f"{colors["red"]}Houve um ERRO ao escrever o arquivo!{colors["none"]}")
        else:
            print(f"Novo registro de {name} adicionado.")
            archive.close()
