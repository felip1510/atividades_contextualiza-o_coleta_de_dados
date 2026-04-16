import random

l = []

for i in range(5):
    producao = round(random.uniform(2, 10), 1)
    l.append(producao)

media = round(sum(l) / 5,2)

if media > 4.8:
    print(media, "média atingida")
else:
    print(media, "média não atingida")