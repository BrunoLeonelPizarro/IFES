
from io import open

# Usando raw string para evitar problemas con las barras invertidas
archivo = open("IFES-3\IFES\ArchivoTxt\documento.txt", "w")
archivo.write("Sr. Juan Carlos \nGerente General \n12 de mayo del 2024")
archivo.close()