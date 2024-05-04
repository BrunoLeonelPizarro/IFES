import os
os.system("cls")

def descuento_por_Cantidad (a,b):
    precio_con_Descuento = (a * b) / 100
    return precio_con_Descuento

def porcentaje_del_descuento (a,b):
    porcentaje = (a * 100) / b
    return porcentaje


precio_producto = int(input("Ingrese el precio del producto: "))
cantidad = int (input("Ingrese La cantidad: "))
precio_Por_Cantidad = precio_producto * cantidad

lista_Descuentos_Por_Cantidad = {"1":descuento_por_Cantidad(precio_Por_Cantidad, 1), "2": descuento_por_Cantidad(precio_Por_Cantidad, 3), "3":descuento_por_Cantidad(precio_Por_Cantidad, 5), "otro":descuento_por_Cantidad(precio_Por_Cantidad, 10)}

if cantidad <= 5:
    precio_Con_Descuento = lista_Descuentos_Por_Cantidad ["1"]
elif cantidad <= 10:
    precio_Con_Descuento = lista_Descuentos_Por_Cantidad ["2"]
elif cantidad <= 15:
    precio_Con_Descuento = lista_Descuentos_Por_Cantidad ["3"]
else:
    precio_Con_Descuento = lista_Descuentos_Por_Cantidad ["otro"]

precio_Final = precio_Por_Cantidad - precio_Con_Descuento

print("el precio del producto es de", precio_producto,"$ por", cantidad, "unidades", "da un total de", precio_Por_Cantidad ,"el descuento por cantidad seria del", porcentaje_del_descuento(precio_Con_Descuento, precio_Por_Cantidad), "% de descuento y asi dando un total de", precio_Final)