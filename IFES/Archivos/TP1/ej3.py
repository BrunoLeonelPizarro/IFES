from io import open
import os

os.system("cls")

#archivo = open("IFES\TP1\Ejercicio1\Doc1.txt","a")
#archivo.write("\n\n Nos dirigimos a Ud...")

archivo = open("IFES\TP1\Ejercicio1\Doc1.txt", "r")
contenido = archivo.readlines()
#for i in contenido:
    # datos = i.split(";")
    #print(datos[0])

for i in range (30):
    os.system("cls")
    archivo.seek(i)
    contenido=archivo.read()
    print(contenido)
    letra = input("Ingrese para continuar: ")

archivo.close()
