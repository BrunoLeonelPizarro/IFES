import sqlite3
import os

#3. Poder hacer una modificacion SELECT y mostrar el registro

miConexion = sqlite3.connect("IFES/BaseDatos/TP1/Base2")
miCursor = miConexion.cursor()

print("Antes de actializar")

miCursor.execute("SELECT * FROM ALUMNOS")
datos = miCursor.fetchall()
for dato in datos:
    print(dato[0],"  ",dato[1],"    ",dato[2],"    ",dato[3], "     ", dato[4])

input("Presione enter para actualizar")

miCursor.execute("UPDATE ALUMNOS SET SEDE = 'Cipolletti' WHERE LEGAJO = 'FAI-2232'")
miConexion.commit()

print("Despues de actializar")

miCursor.execute("SELECT * FROM ALUMNOS")
datos = miCursor.fetchall()
for dato in datos:
    print(dato[0],"  ",dato[1],"    ",dato[2],"    ",dato[3], "     ", dato[4])

miConexion.close()

