import os
os.system("cls")

def calcIVA (a,b):
    monto_con_IVA = (a*b/(100)) + a
    return monto_con_IVA

print("Ingrese los datos de la compra: ")
factura_Sin_IVA = int(input("Ingrese el total de la factura sin aplicar el IVA: "))
porcentaje_IVA = int(input("Ingrese el porcentaje del IVA: "))

factura_Con_IVA = calcIVA (factura_Sin_IVA, porcentaje_IVA)

print ("El total a pagar con IVA es de: ", factura_Con_IVA,"$")