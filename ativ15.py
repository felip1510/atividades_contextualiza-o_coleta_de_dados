import random

dados = []

for i in range(100):
    valor = round(random.uniform(1, 10), 1)
    dados.append(valor)

criticos = []

for valor in dados:
    if valor > 9:
        criticos.append(valor)

print("Dados críticos:", criticos)