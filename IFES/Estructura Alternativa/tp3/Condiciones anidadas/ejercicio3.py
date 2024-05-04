import os
os.system("cls")

def calc_Descuentos (a,b):
    descuento = ((a*b) /100)
    return descuento
def porcentaje_Descuento (a,b):
    porcentaje = (a*100)/b
    return porcentaje

precio_Producto = int(input("Ingrese el precio: "))
cod_Descuento = int(input ("Ingrese el codigo de descuento: "))

lista_Descuentos = {"1":calc_Descuentos(precio_Producto, 1), "2":calc_Descuentos(precio_Producto, 3), "3":calc_Descuentos(precio_Producto,5), "otro":calc_Descuentos(precio_Producto, 10)}

def descuento_Eleccion(a):
    if a == 1:
        valor_Con_Descuento = lista_Descuentos["1"]
    elif a == 2:
        valor_Con_Descuento = lista_Descuentos["2"]
    elif a == 3:
        valor_Con_Descuento = lista_Descuentos["3"]
    else:
        valor_Con_Descuento = lista_Descuentos ["otro"]
    return valor_Con_Descuento

precio_Con_Descuento = descuento_Eleccion(cod_Descuento)

precio_Final = precio_Producto - precio_Con_Descuento


print ("el producto con el", porcentaje_Descuento(precio_Con_Descuento, precio_Producto),"% de descuento es de", precio_Final)