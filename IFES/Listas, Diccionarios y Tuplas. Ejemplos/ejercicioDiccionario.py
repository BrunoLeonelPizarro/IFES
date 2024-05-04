import os
os.system("cls")

def llaves_Diccionario (a):
    llaves = a.keys()
    return llaves

def valores_Diccionario (a):
    valores = a.values()
    return valores

#-----------------------------------#
diccionario1 = {"PGM":"Programacion", "IC":"Introduccion a la computacion", "MD":"Modelar datos", "SO":"Sistemas operativos", "ALG":"Algebra", "TC":"Teoria de la computacion", "DW":"Desarollo Web"}
print(diccionario1);input()
#-----------------------------------#
diccionario1["ALGL"] = "Algebra lineal"
diccionario1["MSI"] = "Modelado de sistemas de informacion"
print(diccionario1);input()
#-----------------------------------#

#-----------------------------------#
diccionario1 ["MD"]= "Modelado de datos" 
#-----------------------------------#

#-----------------------------------#
print(llaves_Diccionario(diccionario1));input()
#-----------------------------------#
#-----------------------------------#
print(valores_Diccionario(diccionario1));input()
#-----------------------------------#

