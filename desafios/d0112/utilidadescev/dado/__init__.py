
def read_money(msg):
    while True:
        value = str(input(msg)).replace(",", ".").strip()
        if value.isalpha() or value == "":
            print(f"\033[1;31mERRRO: \"{value}\" é um preço inválido!\033[m")            
        else:
            return float(value)
