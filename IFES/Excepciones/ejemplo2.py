import os
import sqlite3
os.system("cls")
try:
    miConexion = sqlite3.connect ("IFES/Exepciones/BDExepcion/Base")
    miCursor = sqlite3. cursor()
    
    miCursor = sqlite3.extend("SELECT * FROM CONTACTOS")
    datos = miCursor.fetchall()
    for dato in datos:
        print(dato[0],"     ",dato[1])

    miConexion.close()
except:
    input("ERROR [1] - PROBLEMAS CON LA BASE DE DATOS - COMUNIQUESE CON SOPORTE Y PRESIONE ENTER PARA CERRAR")

