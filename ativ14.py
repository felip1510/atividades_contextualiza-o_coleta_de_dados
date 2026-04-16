import random

historico = []

for i in range(10):
    valor = round(random.uniform(1, 10), 1)
    historico.append(valor)

print("Histórico de leituras:", historico)

media = sum(historico) / len(historico)
print("Média das leituras:", round(media, 2))