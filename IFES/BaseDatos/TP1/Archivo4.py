#4. Hacer un select para poder eliminar o modificar un registro

import sqlite3
import os

miConexion = sqlite3.connect("IFES/BaseDatos/TP1/Base2")
miCursor = miConexion.cursor()

print("Antes de actializar")

miCursor.execute("SELECT * FROM ALUMNOS")
datos = miCursor.fetchall()
for dato in datos:
    print(dato[0],"  ",dato[1],"    ",dato[2],"    ",dato[3], "     ", dato[4])
input("Presione enter para BORRAR")

miCursor.execute("DELETE FROM ALUMNOS WHERE LEGAJO = 'FAI-1232'")
miConexion.commit()

print("ALUMNO ELIMINADO")

miCursor.execute("SELECT * FROM ALUMNOS")
datos = miCursor.fetchall()
for dato in datos:
    print(dato[0],"  ",dato[1],"    ",dato[2],"    ",dato[3], "     ", dato[4])

miConexion.close()

