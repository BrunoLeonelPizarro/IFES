import os
os.system("cls")

def operacionUNO (a, b):
    multiplicacion = a*b
    return multiplicacion

def operacionDos (a):
    operacion2 = (a**2)*(a*a)
    return operacion2

def operacionTres (a,b):
    operacion3 = (a+b)/b
    return operacion3

def operacionCuatro (a, b):
    operacion4 = (a**2)+(b**2)*(a*a+b*b)
    return operacion4


def operacionCinco (a, b):
    operacion5 = 2*a + b/2
    return operacion5

print("Ingrese los siguientes datos: ")

numero_A = int(input("Ingrese el valor del numero A: "))
numero_B = int(input("\nIngrese el valor del numero B: "))

operacion_1 = operacionUNO (numero_A, numero_B)
operacion_2 = operacionDos (numero_A)
operacion_3 = operacionTres (numero_A, numero_B)
operacion_4 = operacionCuatro (numero_A, numero_B)
operacion_5 = operacionCinco(numero_A, numero_B)

print ("\nOperacion A*B:", operacion_1)
print("\nOperacion A2(A*A):", operacion_2)
print("\nOperacion (A+B)/B:", operacion_3)
print ("\nOperacion A2 + B2 (A*A + B*B): ", operacion_4)
print ("\nOperacion 2*A + 2*B: ", operacion_5)