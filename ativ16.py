import random
import time

for i in range(10):
    valor = round(random.uniform(1, 10), 1)
    print("Dado gerado:", valor)
    
    # Simula envio para nuvem
    time.sleep(0.5)
    print("Enviado para a nuvem:", valor)
    print("---")