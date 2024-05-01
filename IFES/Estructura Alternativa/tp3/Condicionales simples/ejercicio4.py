import os
os.system("cls")

apellido = input("Ingrese su apellido: ")
Localidad = input("Ingrese su Localidad: ")

if Localidad == "neuquen":
    print("Bienvenido!", apellido)
else:
    print ("Al parecer sos de", Localidad)