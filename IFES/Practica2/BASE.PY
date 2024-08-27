import sqlite3

miconexion = sqlite3.connect("IFES/Practica2/BDP/BasePreactica")
micursor = miconexion.cursor()
micursor.execute("CREATE TABLE CONTACTOS(NOMBRE VARCHAR(50), TELEFONO VARCHAR(50))")
miconexion.close()