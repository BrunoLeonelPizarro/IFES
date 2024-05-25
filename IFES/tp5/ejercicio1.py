import os
os.system("cls")

apellido = []
asignatura = []

for i in range (5):
    os.system("cls")
    print("Ingrese los datos del estudiante ",i+1)
    apellido.append(input("Ingrese el apellido: ").capitalize())
    asignatura.append(input("Ingrese la asignatura: "))
os.system("cls")
print("======================= MUESTREO DE DATOS ================================")
for i in range (5):
    print("Apellido: ",apellido[i],"| Asignatura: ", asignatura [i])
    print("=========================================")