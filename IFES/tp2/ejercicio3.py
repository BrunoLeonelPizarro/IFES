import os
os.system("cls")

def calcAreaTriangulo (a,b):
    area_triangulo = (a*b)/2
    return area_triangulo

def calcPerimetro (a, b, c):
    
    perimetro_triangulo = a + b + c 
    return perimetro_triangulo


print("Ingrese los datos del triangulo equilatero: ")
lado1 = int(input("ingrese la medida del lado del 1 triangulo: "))
lado2 = int(input("\ningrese la medida del lado del 2 triangulo: "))
lado3 = int(input("\ningrese la medida del lado del 3 triangulo: "))

base_Triangulo = int(input("\nIngrese la medida de la base: "))
altura_Triangulo = int (input("Ingrese la medida de la altura: "))

perimetro = calcPerimetro (lado1, lado2, lado3)
area = calcAreaTriangulo (base_Triangulo, altura_Triangulo)

print("\n------------------------------°---------------------------------------")
print("\nArea triangulo:", area)
print("perimetro: ", perimetro)
