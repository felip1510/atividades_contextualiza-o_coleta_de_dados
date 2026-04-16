import random
l=[]
for i in range (10):
    dados = round(random.uniform (3, 10),1)
    l.append(dados)

soma = sum (l)
eficiencia = round(soma,1)
print (eficiencia,"% de eficiencia")
print ("Meta: 70% - 100%")
if eficiencia >= 70:
    print("meta alcançada!")
elif eficiencia < 70:
    print("meta não alcançada!")