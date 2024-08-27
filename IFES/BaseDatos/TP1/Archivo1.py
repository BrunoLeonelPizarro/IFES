import sqlite3
import os

#Crear una BD que tenga 4 campos e insertar 5 registros, mostrar la estructura en DB browse y en ola terminal y despues eliminar 1 registro

#1. Creacion de BD, fijar si se crea
#2. Hacer un insert de 5 registros, hacer un select para ver si tomo los registros
#3. Poder hacer una modificacion SELECT y mostrar el registro
#4. Hacer un select para poder eliminar o modificar un registro

miConexion = sqlite3.connect("IFES/BaseDatos/TP1/Base2")
miCursor = miConexion.cursor()
miCursor.execute("CREATE TABLE ALUMNOS (NOMBRE VALCHAR(50), APELLIDO VALCHAR(50), SEDE VALCHAR(50), DNI INTEGRER, LEGAJO VALCHAR(50))")
miConexion.close