import os
os.system("cls")

def desicion_Numeros (a):
    if a > 0:
        cartel = "El numero es positivo"
    else:
        cartel = "El numero es negativo"
    return cartel

numero = int(input("Ingrese un numero: "))

print(desicion_Numeros(numero))