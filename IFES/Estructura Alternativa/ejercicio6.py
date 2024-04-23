import os
os.system("cls")

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
cod_Categoria = input("Ingrese la categoria del trabajador: ")

if cod_Categoria == "A":
    categoria = "Vendedor"
    sueldo = 750000
    print("El trabajador", nombre, apellido, "de la categoria", categoria, "tiene un salario de:", sueldo)
elif cod_Categoria == "B":
    categoria = "Administrativo"
    sueldo = 820000
    print("El trabajador", nombre, apellido, "de la categoria", categoria, "tiene un salario de:", sueldo)
elif cod_Categoria == "C":
    categoria = "Cajero"
    sueldo = 780000
    print("El trabajador", nombre, apellido, "de la categoria", categoria, "tiene un salario de:", sueldo)

else:
    print("Categoria Invalida")