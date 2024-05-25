import os
os.system("cls")

apellido = []
primera_Nota = []
segunda_Nota = []
promedios = []
cantidad_Estudiantes = 5


for i in range (cantidad_Estudiantes):
    print("Ingrese los datos del estudiante", i+1)
    apellido.append(input("Ingrese el apellido del estudiante: ").upper())
    primera_Nota.append(int(input("Ingrese la primera nota: ")))
    segunda_Nota.append(int(input("Ingrese la segunda nota: ")))
    promedios.append((primera_Nota[i] + segunda_Nota[i]) / 2) 
os.system("cls")
for i in range (cantidad_Estudiantes):
    print("Alumno N°:",i+1,"|Apellido: ",apellido[i], "| Nota 1: ",primera_Nota[i],"| Nota 2: ",segunda_Nota[i], "| Promedio: ",promedios[i])