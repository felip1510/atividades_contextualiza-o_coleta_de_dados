import random

for i in range (20):
    consumo = round(random.uniform (10, 100),2)
    if consumo > 65:
        print("Consumo elevado",consumo)
        print("\n")
    else:
        print(consumo)
        print("\n")