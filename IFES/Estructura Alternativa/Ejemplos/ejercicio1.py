import os
os.system("cls")

print("Ingrese los soguientes datos:")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese apellido: ")

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Bienvenido ", nombre)

else:
    print("Bienvenido ", apellido)
