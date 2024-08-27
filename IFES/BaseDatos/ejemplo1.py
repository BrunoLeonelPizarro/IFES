import sqlite3 

miConexion = sqlite3.connect("IFES/BaseDatos/BD/Base1")
micursor = miConexion.cursor()
micursor.execute("CREATE TABLE CONTACTOS(NOMBRE VARCHAR(50), TELEFONO INTEGRER)")
miConexion.close()