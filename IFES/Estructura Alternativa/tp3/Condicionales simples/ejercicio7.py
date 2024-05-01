import os
import random
os.system ("cls")

print("Presioone enter para tirar el primer dado");input()
tirada_Dado_Uno = random.randint(1,6)
print("El resultado es un:", tirada_Dado_Uno)
print("\nPresioone enter para tirar el segundo dado");input()
tirada_Dado_Dos = random.randint(1,6)
print("El resultado es un:", tirada_Dado_Dos)

if tirada_Dado_Uno == tirada_Dado_Dos:
    print("\nLos dados son Iguales!!")
else:
    print("\nLos dados no son iguales :(")