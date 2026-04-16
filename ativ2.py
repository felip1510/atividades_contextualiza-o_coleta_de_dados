import random

for i in range (20):
    ms = round(random.uniform (0, 2),2)
    if ms < 0.5:
        print("Alerta",ms,"m/s")
        print("\n")
    else:
        print(ms)
        print("\n")