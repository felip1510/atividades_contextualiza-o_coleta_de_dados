import random
import time
armazenamento=[]
for i in range (10):
    dados = round(random.uniform (20, 70),1)
    armazenamento.append(dados)
    if dados > 50:
        time.sleep(0.7)
        print ("-",dados,"graus, temperatura elevada!")
        print ("- DESLIGANDO...")
        print ("\n")
    else:
        time.sleep(0.7)
        print ("-",dados,"graus, temperatura aceitavel!")
        print ("\n")
print("----------------------------------------------------------------------------")
time.sleep(0.7)    
print("dados gerados:",armazenamento)
print("----------------------------------------------------------------------------")

alertas = []

time.sleep(0.7)
for dados in armazenamento:
    if dados > 50:
        alertas.append(dados)

print("Temperaturas elevadas:", alertas)
print("----------------------------------------------------------------------------")

normais = []

time.sleep(0.7)
for dados in armazenamento:
    if dados <= 50:
        normais.append(dados)

print("Temperaturas aceitaveis:", normais)
print("----------------------------------------------------------------------------")