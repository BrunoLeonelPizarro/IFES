import os
import sqlite3

os.system("cls")

miConexion = sqlite3.connect("IFES/BaseDatos/BD/Base1")
miCursor = miConexion.cursor()
print("Datos Originales")
miCursor.execute("SELECT * FROM CONTACTOS")
datos = miCursor.fetchall()
for dato in datos:
    print(dato[0],"     ",dato[1])
input("Presione una tecla")

miCursor.execute("DELETE FROM CONTACTOS WHERE NOMBRE ='Juan'")
miConexion.commit()

os.system("cls")
print("DATOS ACTUALIZADOS")
miCursor.execute("SELECT * FROM CONTACTOS")
datos = miCursor.fetchall()
for dato in datos:
    print(dato[0],"     ",dato[1])
miConexion.close()