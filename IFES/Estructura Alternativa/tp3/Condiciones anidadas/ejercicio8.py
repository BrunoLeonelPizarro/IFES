import os
os.system("cls")

lista_Clubes = ["Norte", "Sur", "Este", "Oeste"]
diccionario_Categoria_Por_Edades = {"menores de 13":"Menores", "Menores de 16":"Cadetes", "Menores de 25":"Mayores", "Otra":"Adultos"}

def definir_Categoria (a):
    if a <= 13:
        categoria_Definida = diccionario_Categoria_Por_Edades["menores de 13"]
    elif a <= 16:
        categoria_Definida = diccionario_Categoria_Por_Edades["Menores de 16"]
    elif a <= 25:
        categoria_Definida = diccionario_Categoria_Por_Edades ["Menores de 25"]
    else:
        categoria_Definida = diccionario_Categoria_Por_Edades ["Otra"]
    return categoria_Definida

def definir_Club (a):
    if a == diccionario_Categoria_Por_Edades["menores de 13"]:
        club_Definido = lista_Clubes[0]
    elif a == diccionario_Categoria_Por_Edades ["Menores de 16"]:
        club_Definido = lista_Clubes [1]
    elif a == diccionario_Categoria_Por_Edades ["Menores de 25"]:
        club_Definido = lista_Clubes[2]
    else:
        club_Definido = lista_Clubes[3]
    return club_Definido



edad = int(input("ingrese la edad: "))

categoria = definir_Categoria(edad)
club = definir_Club(categoria)

print ("El aspirante tiene", edad ,"años de edad por lo que pertenece a la categoria de los", categoria ,"por lo que se lo asigna al club", club)

