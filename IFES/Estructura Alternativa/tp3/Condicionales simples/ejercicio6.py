import os
import random
os.system ("cls")

lista_desiciones = ["Cara", "Cruz"]

print("Presione enter para tirar la moneda");input()
randomizador = random.randint(1,2)

if randomizador == 1:
    
    print("Salio", lista_desiciones[0])
else:
    print ("Salio", lista_desiciones[1])