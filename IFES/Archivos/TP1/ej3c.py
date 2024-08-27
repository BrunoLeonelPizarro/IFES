from io import open
import os
os.system("cls")

archivo = open("IFES\TP1\Ejercicio1\Doc2.txt", "w")
archivo.write("La ciencia no es mas que perversion en si misma a menos que tenga como objetivo ultimo mejorar la humanidad.")

archivo = open("IFES\TP1\Ejercicio1\Doc2.txt", "r")
contenido = archivo.readline()

for i in range (20):
    archivo.seek(i)
    

contenido = archivo.read()
print(contenido)
archivo.close()