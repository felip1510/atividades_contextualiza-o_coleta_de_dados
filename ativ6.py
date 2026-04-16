import random

for i in range (10):
    nivel = round(random.uniform (0, 100),2)
    if nivel > 90 or nivel < 20:
        print("ALERTA",nivel,"% de fluido")
        print("\n")
    else:
        print(nivel)
        print("\n")