
import math
print("CALCULANDO HIPOTENUSA")
cateto_oposto = float(input("digite o valor do cateto oposto: "))
cateto_adjacente = float(input("digite o valor do cateto adjacente: "))

#hipotenusa = math.sqrt(math.floor(cateto_oposto)**2 + math.floor(cateto_adjacente)**2)

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f"o valor da hipotenusa é igual a {hipotenusa:.2f}")
