import random
import time

while True:
    valor = round(random.uniform(1, 10), 1)
    
    if valor <= 7:
        estado = "normal"
    elif valor <= 8.5:
        estado = "alerta"
    else:
        estado = "crítico"
    
    print(valor, "->", estado)
    time.sleep(1)