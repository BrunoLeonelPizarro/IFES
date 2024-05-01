import os
os.system("cls")

apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo: ")

if sexo == "Femenino":
    print ("Bienvenida! ", apellido)
else:
    print("Su edad es:", edad)