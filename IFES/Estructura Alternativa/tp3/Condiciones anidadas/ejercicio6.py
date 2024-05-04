import os
os.system("cls")

Diccionario_Materias = {"I": "Introduccion", "S": "Sistemas", "M":"Matematica", "Otra": "Ingles"}

def definicion_Materias_Por_Codigo (a):
    if a == "I":
        materia = Diccionario_Materias["I"]
    elif a == "S":
        materia = Diccionario_Materias["S"]
    elif a == "M":
        materia = Diccionario_Materias ["M"]
    else:
        materia = Diccionario_Materias["Otra"]
    return materia

apellido = input("Ingrese el apellido: ")
codigo_Materia = input("Ingrese el codigo de la materia: ")

materia_Seleccionada = definicion_Materias_Por_Codigo (codigo_Materia)

print("El estudiante", apellido, "Esta cursando la materia", materia_Seleccionada)