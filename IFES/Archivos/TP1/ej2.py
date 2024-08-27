from io import open
import os

os.system("cls")

archivo = open("IFES\Archivos\TP1\Doc1.txt", "r")
contenido = archivo.readlines()
archivo.close()
print("-"*20)
for i in range (3):
    print(contenido[i])