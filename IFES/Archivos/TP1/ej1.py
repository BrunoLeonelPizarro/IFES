from io import open
import os

os.system("cls")

archivo = open("IFES\Archivos\TP1\Doc1.txt", "w")
archivo.write("Primer Linea. \n")
archivo.write("Segunda Linea. \n")
archivo.write("Tercera Linea. \n")

archivo.close()

archivo = open("IFES\Archivos\TP1\Doc1.txt", "r")
contenido = archivo.read()
archivo.close
print("-"*20)
print(contenido)


