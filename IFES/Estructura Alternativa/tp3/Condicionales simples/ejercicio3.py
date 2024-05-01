import os
os.system ("cls")

def resta_Numeros (a,b):
    if a > b:
        operacion_Resta = a - b
    else:
        operacion_Resta = b - a
    return operacion_Resta

numero_Uno = int(input("Ingrese el numero uno: "))
numero_Dos = int(input("Ingrese el numero dos: "))

print("La resta del numero mas grande menos el chico da como resultado:", resta_Numeros (numero_Uno, numero_Dos)) 