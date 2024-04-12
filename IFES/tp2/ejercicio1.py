#Calculo Factura
import os
os.system("cls")


#---------------Caegar datos Cliente---------------------#
print("Ingrese los datos del ciente:")
nombre_Cliente = input("Ingrese el nombre: ")
apellido_Cliente = input("Ingrese el apellido: ")
DNI_Cliente = int(input("Ingrese el numero de D.N.I: "))
#--------------------------------------------------------#

#-------------------Cargar datos Compra--------------------------------------#
print ("Ingrese los datos de la compra")
nombre_Pri_Producto = input("Ingrese el nombre del primer producto: ")
precio_pri_producto = int(input("Ingrese el precio del primer producto: "))
cantidad_pri_producto = int(input("Ingrese la cantidad del primer producto: "))
precio_pri_producto = precio_pri_producto * cantidad_pri_producto

nombre_Seg_Producto = input("Ingrese el nombre del segundo producto: ")
precio_Seg_producto = int(input("Ingrese el precio del segundo producto: "))
cantidad_Seg_producto = int(input("Ingrese la cantidad del segundo producto: "))
precio_Seg_producto = precio_Seg_producto * cantidad_Seg_producto
#-------------------------------------------------------------------------------#

#---------------------Funcion IVA----------------------#
def IVA (a, b):
    iva = ((a*21)/100) + ((b*21)/100)
    return iva
#------------------------------------------------------#

#-------------------Calculo factura------------------------------------------#
subtotalProducto = precio_pri_producto + precio_Seg_producto

ivaTotal = IVA (precio_pri_producto, precio_Seg_producto)

importe_total = subtotalProducto + ivaTotal
#----------------------------------------------------------------------------#


print("Facturacion compra:")
print("Cliente:", nombre_Cliente, apellido_Cliente, "DNI:", DNI_Cliente)
print("Datos de factura: ")
print("Nombre primer producto:", nombre_Pri_Producto, "Cantidad:", cantidad_pri_producto, "precio x unidad:", precio_pri_producto / cantidad_pri_producto)
print("Nombre segundo producto:", nombre_Seg_Producto, "Cantidad:", cantidad_Seg_producto, "precio x unidad:", precio_Seg_producto/ cantidad_Seg_producto)
print("SubTotal de la compra: ", subtotalProducto)
print("Precio total de la compra: ", importe_total)