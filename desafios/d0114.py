
"""
    Crie um código em python que teste se o site pudim está acessível pelo computador usado.
"""

import requests
from funcoes_globais import titulo

titulo("SITE ESTÁ ACESSÍVEL ?")

def site_acessivel(url, timeout=5):
    try:
        resposta = requests.get(url, timeout=timeout)
    except requests.exceptions.RequestException:
        print(f"{url} etá fora do ar")    
    else:
        print(f"{url} está acessível")
        return resposta.status_code < 400

site_acessivel("https://www.pudim.com.br")