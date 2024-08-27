import sqlite3
import os

miConexion = sqlite3.connect("IFES/BaseDatos/TP1/Base2")
miCursor = miConexion.cursor()

miCursor.execute("INSERT INTO ALUMNOS VALUES ('Jose','Luis','Neuquen',44567845,'FAI-2232')")
miConexion.commit()
miCursor.execute("INSERT INTO ALUMNOS VALUES ('Manuel','Ocampo','Rio Negro',42667345,'FAI-2432')")
miConexion.commit()
miCursor.execute("INSERT INTO ALUMNOS VALUES ('Luis','Manuel','Cipolletti',34567845,'FAI-1232')")
miConexion.commit()
miCursor.execute("INSERT INTO ALUMNOS VALUES ('Paula','Ojeda','Neuquen',46767845,'FAI-2342')")
miConexion.commit()
miCursor.execute("INSERT INTO ALUMNOS VALUES ('Alberto','Santoro','Rio Negro',47000845,'FAI-2000')")
miConexion.commit()

miConexion.close()