import os
os.system("cls")

def definir_Pelicula (a):
    if a <= 13:
        pelicula_Definida = diccionario_Peliculas_Horarios ["Menores de 13"]
    elif a <= 16:
        pelicula_Definida = diccionario_Peliculas_Horarios ["Menores de 16"]
    elif a <= 25:
        pelicula_Definida = diccionario_Peliculas_Horarios ["Menores de 25"]
    else:
        pelicula_Definida = diccionario_Peliculas_Horarios ["Otros"]
    return pelicula_Definida

def definir_Horrario (a):
    if a == diccionario_Peliculas_Horarios ["Menores de 13"]:
        horario_definido = lista_horarios [0]
    elif a == diccionario_Peliculas_Horarios ["Menores de 16"]:
        horario_definido = lista_horarios [1]
    elif a == diccionario_Peliculas_Horarios ["Menores de 25"]:
        horario_definido = lista_horarios [2]
    else:
        horario_definido = lista_horarios [3]
    return horario_definido

lista_horarios = ("15:00", "17:00", "19:00","21:00")
diccionario_Peliculas_Horarios = {"Menores de 13": "Los increibles 3", "Menores de 16":"Buscando a nemo", "Menores de 25":"Rapido y Furiosos 7", "Otros": "La Verdad Oculta"}

edad = int(input("Ingrese la edad: "))

pelicula = definir_Pelicula(edad)
horario = definir_Horrario(pelicula)

print("La pelicula disponible para la edad de", edad , "de edad es la de", pelicula ,"a las", horario, "horas")

