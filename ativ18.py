import random
l=[]
for i in range (10):
    dados = round(random.uniform (2, 10),2)
    if dados <= 4: 
        print("anomalia detectada",dados)
    l.append(dados)

print (l)