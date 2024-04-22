import os
os.system("cls")

def desicion_Numeros (a,b):
    if a > b:
        cartel ="El mayor es el primer numero"
    else:
        cartel = "El mayor es el segundo numero"
    return cartel

print("Ingrese los siguientes datos: ")
numero_Uno = int(input("Ingrese el primer numero: "))
numero_Dos = int(input("Ingrese el segundo numero: "))

print(desicion_Numeros (numero_Uno, numero_Dos)) 
