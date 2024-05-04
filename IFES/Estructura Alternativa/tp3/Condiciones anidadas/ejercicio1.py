import os
os.system("cls")

def opracion_Numeros (a):
    if a == 0:
        nuevo_Num = a-1
    elif a > 0:
        nuevo_Num = a*2
    else:
        nuevo_Num = a/2
    return nuevo_Num

numero_Ingresado = input("Ingrese un numero")

numero_operado = opracion_Numeros (numero_Ingresado)

print(numero_operado)

