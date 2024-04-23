import os
os.system("cls")

def calc_Promedio (a,b):
    promedio = (a + b)/2
    return promedio

def desicion_Nota (a):
    if a <= 2:
        cartel ="Insuficiente"
    elif a <= 4:
        cartel = "Libre"
    elif a <= 6:
        cartel = "Regular"
    elif a >= 7:
        cartel = "Promocion"
    return cartel

print("Ingrese las notas a cargar: ")
nota_Uno =int(input("\nIngrese la primera nota: "))
nota_Dos =int(input("Ingrese la segunda nota: "))

print("\nEl promedio del alumno es de", calc_Promedio(nota_Uno, nota_Dos),"lo pone en condicion" , desicion_Nota(calc_Promedio(nota_Uno, nota_Dos)))