import os
os.system ("cls")

def suma_Numeros (a,b):
    if a + b > 100:
        numero_Seleccionado = a
    else:
        numero_Seleccionado = b
    return numero_Seleccionado


numero_Uno = int(input("Ingrese el numero uno"))
numero_Dos = int(input("Ingrese el numero dos"))

print(suma_Numeros(numero_Uno, numero_Dos))