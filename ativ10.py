import random

for i in range (10):
    temperatura = round(random.uniform (15, 100),2)
    if temperatura > 80:
        print(temperatura,"!TEMPERATURA ALTA DESLIGAMENTO AUTOMATICO!")
        print("\n")
    else:
        print(temperatura,"temperatura padrão operação normal")
        print("\n")