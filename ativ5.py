import random

for i in range (10):
    temperatura = round(random.uniform (0, 15),2)
    if temperatura > 10:
        print(temperatura,"!TEMPERATURA ELEVADA!")
        print("\n")
    else:
        print(temperatura)
        print("\n")