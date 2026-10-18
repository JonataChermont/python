
def titulo(texto, linha="="):
    tamanho_texto = len(texto) * 2
    if len(texto) % 2 == 1:
        print(f"{linha * (tamanho_texto - 1)}\n{texto.center(tamanho_texto)}\n{linha * (tamanho_texto - 1)}")    
    else:
        print(f"{linha * tamanho_texto}\n{texto.center(tamanho_texto)}\n{linha * tamanho_texto}")
