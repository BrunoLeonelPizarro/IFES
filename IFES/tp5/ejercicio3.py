import os
os.system("cls")

apellido = []
nombre = []
localidad = []
cantidad_Inscriptos = 2
print("Ingrese los datos solicitados")
for i in range (cantidad_Inscriptos):
    print("ID N°", i+1)
    apellido.append(input("Ingrese el apellido: ").upper())
    nombre.append(input("Ingrese su nombre: ").capitalize())
    localidad.append(input("Ingrese el nombre de su localidad: ").lower())
    os.system("cls")
for i in range (cantidad_Inscriptos):
    print("ID N°:",i+1,"| Apellido: ",apellido[i],"| Nombre: ",nombre[i],"| Localidad: ",localidad[i])
    print("=====================================")