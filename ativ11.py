import random

leituras = []
falhas = 0

for i in range(7):
    valor = round(random.uniform(1, 10), 1)
    leituras.append(valor)
    
    if valor < 2.0 or valor > 8.0:
        print("Alerta! Leitura fora do padrão:", valor)
        falhas += 1

print("Todas as leituras:", leituras)
print("Número total de falhas:", falhas)