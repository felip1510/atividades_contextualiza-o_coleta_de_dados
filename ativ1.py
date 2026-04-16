import random

for i in range (20):
    temperatura = round(random.uniform (30, 100),2)
    if temperatura > 80:
        print(temperatura,"!TEMPERATURA ELEVADA!")
        print("\n")
    else:
        print(temperatura)
        print("\n")