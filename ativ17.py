import random
l=[]
for i in range (10):
    dados = round(random.uniform (2, 10),2)
    l.append(dados)
media = round(sum(l)/len(l),2)
maximo = max(l)
minimo = min(l)
print ("Sua media é:",media)
print ("Valor maximo é:",maximo)
print ("Valor minimo é:",minimo)