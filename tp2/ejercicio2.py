#Ejercicio 2
import os
os.system("cls")


def calcDescuento(a):
    valordescuento = ((a*5)/100)
    descuento_Apricado = a - valordescuento
    return descuento_Apricado


importe_Total = int(input("Ingrese el monto total: "))
importe_Total = calcDescuento(importe_Total)
print("El importe con el descuento del 5% aplicado es de:", importe_Total)





