import os
os.system("cls")
contador = 0
for i in range(5):
    edad = int(input("Ingrese la edad (Entre 18 y 50 años): "))
    
    while edad<18 or edad >50:
        os.system("cls")
        print ("----------------ERROR----------------")
        edad = int(input("Ingrese una edad entre 18 a 50 años: "))
        print("--------------------------------------")
    if edad < 30:
        categoria_Edad = "Menor"
    else:
        categoria_Edad = "Mayor"
    categoria = input("Ingrese una categoria: ")
    #-----------------------------------------------------------------------#
    while categoria == "A" and categoria == "B" and categoria == "C":
        print ("----------------ERROR----------------")
        categoria = (input("Ingrese una categoria correcta: "))
        print("--------------------------------------")
    if categoria == "A":
        categoria_Asignada = "Vendedor"
    elif categoria == "B":
        categoria_Asignada = "Cajero"
    elif categoria == "C":
        categoria_Asignada = "Administracion"
    localidad = input("Ingrese una localidad: ")
    if localidad == "C":
        localidad_Asignada = "Cipoletti"
    elif localidad == "N":
        localidad_Asignada = "Neuquen"
    elif localidad == "R":
        localidad_Asignada = "Roca"
    elif localidad == "A":
        localidad_Asignada = "Allen"
    
    importe = int(input("Ingrese el importe: "))
    while importe<1000 or importe >5000:
        os.system("cls")
        print ("----------------ERROR----------------")
        edad = int(input("Ingrese un importe entre 1000 a 5000: "))
        print("--------------------------------------")
    codigo = int(input("Ingrese el codigo: "))
    while codigo == 1 and codigo == 2 and codigo == 3:
        os.system("cls")
        print ("----------------ERROR----------------")
        edad = int(input("Ingrese un codigo valido (1, 2, o 3): "))
        print("--------------------------------------")
    codigo_Materia = input("Ingrese la materia: ")
    nota = int(input("Ingrese la nota: "))
    cod_Carrera = input("Ingrese el codigo de la carrera")
    
    
    os.system
    print("La edad ingresada es de: ",edad," años")