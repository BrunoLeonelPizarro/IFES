import os
os.system("cls")

edad = []
categoria = []
localidad = []
importe = []
codigo = []
materia = []
codigo_Carrera = []



tamaño = 2

for i in range (tamaño):
    
    edad.insert(i(int(input("Ingrese la edad (Entre 18 y 50): "))))
    while edad[i] < 18 or edad[i] > 50:
        os.system("cls")
        print("ERROR EDAD")
        edad.insert(i(int(input("Ingrese la edad (Entre 18 y 50): "))))
        os.system("cls")
        
    categoria.insert(input("Ingrese la categoria (A: Vendedor, B: Cajero, C: Administrador)"))
    while categoria[i] != "A" and categoria[i] != "B" and categoria[i] != "C" and categoria[i] != "a" and categoria[i] != "b" and categoria[i] != "c":
        os.system("cls")
        print("ERROR CATEGORIA")
        categoria.insert(i(input("Ingrese la categoria (A: Vendedor, B: Cajero, C: Administrador)")))
        os.system("cls")
        
    localidad.insert(i(input("Ingrese la localidad (C: Cipolletti, R: Rio Negro, N: Administrador, A: Allen)")))
    while localidad[i] != "C" and localidad[i] != "R" and localidad[i] != "N" and localidad[i] != "A" and localidad[i] != "c" and localidad[i] != "r" and localidad[i] != "n" and localidad[i] != "a":
        os.system("cls")
        print("ERROR lOCALIDAD")
        localidad.insert(i(input("Ingrese la localidad (A: Vendedor, B: Cajero, C: Administrador)")))
        os.system("cls")
    
    importe.insert(i(int(input("Ingrese el impoorte: "))))
    while importe[i] < 1000 or importe[i] > 5000:
        os.system("cls")
        print("ERROR IMPORTE")
        importe.insert(i(int(input("Ingrese el impoorte: "))))
        os.system("cls")
    
    codigo.insert(i((input("Ingrese el codigo: "))))
    
    