import os
os.system("cls")

#ejercicio 4
def calcPerimetro (a,b):
    perimetro = 2*a + 2*b
    return perimetro

def calcArea (a,b):
    area = a*b
    return area


valor_Base = int(input("Ingresar el valor de la base: "))
valor_altura = int(input("Ingresar el valor de la altura: "))
print("\nValores del perimetro y el area: ")
areaCuadrado = calcArea(valor_Base, valor_altura)
perimetroCuadrado = calcPerimetro(valor_Base, valor_altura)
print("Area:", areaCuadrado)
print("perimetro: ",perimetroCuadrado)

