import random

for i in range (10):
    vibraçao = round(random.uniform (10, 100),2)
    if vibraçao > 70:
        print(vibraçao,"!VIBRAÇAO ELEVADA!")
        print("\n")
    else:
        print(vibraçao)
        print("\n")