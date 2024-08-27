import os
import sqlite3

os.system("cls")

miConexion = sqlite3.connect("IFES/BaseDatos/BD/Base1")
miCursor = miConexion.cursor()

miCursor.execute("UPDATE CONTACTOS SET TELEFONO = 1512342 WHERE NOMBRE ='Juan' ")
miConexion.commit()

miCursor.execute("SELECT * FROM CONTACTOS")
datos = miCursor.fetchall()
for dato in datos:
    print(dato[0],"     ",dato[1])
miConexion.close()
