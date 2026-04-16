import random

for i in range (20):
    pH = round(random.uniform (4, 10),2)
    if pH < 6:
        print("Alerta",pH,"pH abaixo")
        print("\n")
    elif pH > 8:
        print("Alerta",pH,"pH acima")
        print("\n")
    else:
        print(pH,"pH ideal")
        print("\n")