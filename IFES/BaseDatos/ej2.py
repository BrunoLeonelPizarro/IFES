import sqlite3

#-------------------Iniciar base de dato---------------#
miconexion = sqlite3.connect("IFES/BaseDatos/BD/Base1")
miCursor = miconexion.cursor()
#------------------------------------------------------#

#-----------------------------------------------------------------#
miCursor.execute("INSERT INTO CONTACTOS VALUES ('Juan', 1512345)")
miconexion.commit()
#-----------------------------------------------------------------#
miCursor.execute("INSERT INTO CONTACTOS VALUES ('Laura', 15255527859 )")
miconexion.commit()

miconexion.close()