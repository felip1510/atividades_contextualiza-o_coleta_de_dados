import random

for i in range (10):
    pressao = round(random.uniform (10, 60),2)
    if pressao > 45 or pressao < 20:
        print(pressao,"!PRESSAO FORA DE FAIXA SEGURA!")
        print("\n")
    else:
        print(pressao)
        print("\n")