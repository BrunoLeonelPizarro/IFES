import os
os.system("cls")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

if edad > 21:
    print(apellido)
else:
    print(nombre)