import os
os.system("cls")

cantidad_categoria_Infantiles = 0
cantidad_categoria_Juveniles = 0
cantidad_categoria_Adultos = 0
cantidad_categoria_Mayores = 0
cantidad_categoria_Veteranos = 0
cantidad_deporte_Futbol = 0
cantidad_deporte_Voley = 0
cantidad_deporte_Handball = 0
cantidad_localidad_de_Cipolletti = 0
cantidad_localidad_de_Neuquen = 0
cantidad_localidad_de_Plottier = 0
cantidad_futbol_veteranos = 0

acum_Cuotas_Categoria_Infantiles = 0
acum_Cuotas_Categoria_Juveniles = 0
acum_Cuotas_Categoria_Adultos = 0
acum_Cuotas_Categoria_Mayores = 0
acum_Cuotas_Categoria_Veteranos = 0
acum_Cuotas_Deporte_Futbol = 0
acum_Cuotas_Deporte_Voley = 0
acum_Cuotas_Deporte_Handball = 0

promedio_cuotas_Infantiles = 0
promedio_cuotas_Juveniles = 0
promedio_cuotas_Adultos = 0
promedio_cuotas_Mayores = 0
promedio_cuotas_Veteranos = 0
promedio_Cuotas_deporte_Futbol = 0
promedio_Cuotas_deporte_Voley = 0
promedio_Cuotas_deporte_Handball = 0
promedio_cuotas = 0

apellidos = []
nombres = []
edades = []
cod_localidad = []
localidades = []

cuotas = []

dias = []
horarrios_Practicas = []
categorias = []

cod_deportes = []
deportes = []


cantidad_Inscriptos = 1
id_inscriptos = []
id_inscripto = 0


for i in range (cantidad_Inscriptos):
    id_inscripto = id_inscripto + 1
    id_inscriptos.append(id_inscripto)
    print ("Id N°: ", id_inscriptos [i] )
    apellidos.append(input("Ingrese su apellido: ").capitalize())
    nombres.append(input("\nIngrese su nombre: ").upper())
    edades.append(int(input("\nIngrese su edad: ")))
    while edades[i] < 12 or edades[i] > 50:
        os.system("cls")
        edades.append(int(input("ERROR EDAD | Ingrese una edad entre 12 y 50 años: ")))
        os.system("cls")
    if edades[i] <= 15:
        dias.append("Viernes")
        horarrios_Practicas.append("17:00")
        categorias.append("Infantil")
        cantidad_categoria_Infantiles = cantidad_categoria_Infantiles + 1
    elif edades[i] <= 18:
        dias.append("Viernes")
        horarrios_Practicas.append("19:00")
        categorias.append("Juveniles")
        cantidad_categoria_Juveniles = cantidad_categoria_Juveniles + 1
    elif edades[i] <= 24:
        dias.append("Viernes")
        horarrios_Practicas.append("21:00")
        categorias.append("Adultos")
        cantidad_categoria_Adultos = cantidad_categoria_Adultos + 1
    elif edades[i] <= 40:
        dias.append("Sabado")
        horarrios_Practicas.append("14:00")
        categorias.append("Mayores")
        cantidad_categoria_Mayores + 1
    else:
        dias.append("Sabado")
        horarrios_Practicas.append("16:00")
        categorias.append("Veteranos")
        cantidad_categoria_Veteranos = cantidad_categoria_Veteranos + 1

    cod_deportes.append(input("Ingrese un codigo de deporte (F: (FUTBOL) | V: (VOLEY) | H: (HANDBALL)): "))
    while cod_deportes[i] != "F" and cod_deportes[i] != "V" and cod_deportes[i] != "H" and cod_deportes[i] != "f" and cod_deportes[i] != "v" and cod_deportes[i] != "h":
        os.system("cls")
        cod_deportes.append(input("ERROR CODIGO DEPORTE | Ingrese un codigo de deporte valido (F: (FUTBOL) | V: (VOLEY) | H: (HANDBALL)) : "))
        os.system("cls")
    
    if cod_deportes[i] == "F" or cod_deportes[i] == "f":
        deportes.append("Futbol")
        cantidad_deporte_Futbol = cantidad_deporte_Futbol + 1
    elif cod_deportes[i] == "V" or cod_deportes[i] == "v":
        deportes.append("Voley")
        cantidad_deporte_Voley = cantidad_deporte_Voley + 1
    elif cod_deportes[i] == "H" or cod_deportes[i] == "h":
        deportes.append("Handball")
        cantidad_deporte_Handball = cantidad_deporte_Handball + 1
    
    cod_localidad.append(input("INGRESE UN CODIGO DE LOCALIDAD (C: CIPOLETTI | N: NEUQUEN | P: PLOTTIER): "))
    while cod_localidad[i] != "C" and cod_localidad[i] != "N" and cod_localidad[i] != "P" and cod_localidad[i] != "c" and cod_localidad[i] != "n" and cod_localidad[i] != "p":
        os.system("cls")
        cod_localidad.append(input("Ingrese un codigo de lOCALIDAD valido (C: CIPOLETTI | N: NEUQUEN | P: PLOTTIER): "))
        os.system("cls")
    
    if cod_localidad[i] == "C" or cod_localidad[i] == "c":
        localidades.append("Cipolletti")
        cantidad_localidad_de_Cipolletti = cantidad_localidad_de_Cipolletti +1
    elif cod_localidad[i] == "N" or cod_localidad[i] == "n":
        localidades.append("Neuquen")
        cantidad_localidad_de_Neuquen = cantidad_localidad_de_Neuquen + 1
    elif cod_localidad[i] == "P" or cod_localidad[i] == "p":
        localidades.append("Plottier")
        cantidad_localidad_de_Plottier = cantidad_localidad_de_Plottier + 1
    
    cuotas.append(int(input("Ingrese el valor de la cuota: ")))
    while cuotas[i] <= 0:
        os.system("cls")
        valor_cuota = int(input("ERROR VALOR CUOTA | Ingrese un valor mayor a 0: "))
        os.system("cls")
        
    if categorias [i] == "Infantil":
        acum_Cuotas_Categoria_Infantiles = acum_Cuotas_Categoria_Infantiles + cuotas[i]
        if cantidad_categoria_Infantiles > 0:
            promedio_cuotas_Infantiles = acum_Cuotas_Categoria_Infantiles / cantidad_categoria_Infantiles
        else:
            promedio_cuotas_Infantiles = 0
    elif categorias[i] == "Juveniles":
        acum_Cuotas_Categoria_Juveniles = acum_Cuotas_Categoria_Juveniles + cuotas[i]
        if cantidad_categoria_Juveniles > 0:
            promedio_cuotas_Juveniles = acum_Cuotas_Categoria_Juveniles / cantidad_categoria_Juveniles
        else:
            promedio_cuotas_Juveniles = 0
    elif categorias[i]== "Adultos":
        acum_Cuotas_Categoria_Adultos = acum_Cuotas_Categoria_Adultos + cuotas[i]
        if cantidad_categoria_Adultos > 0:
            promedio_cuotas_Adultos = acum_Cuotas_Categoria_Adultos / cantidad_categoria_Adultos
        else:
            promedio_cuotas_Adultos = 0
    elif categorias == "Mayores":
        acum_Cuotas_Categoria_Mayores = acum_Cuotas_Categoria_Mayores + cuotas[i]
        if cantidad_categoria_Mayores > 0:
            promedio_cuotas_Mayores = acum_Cuotas_Categoria_Mayores / cantidad_categoria_Mayores
        else:
            promedio_cuotas_Mayores = 0
    elif cantidad_categoria_Veteranos == "Veteranos":
        acum_Cuotas_Categoria_Veteranos + acum_Cuotas_Categoria_Veteranos + cuotas[i]
        if cantidad_categoria_Veteranos > 0:
            promedio_cuotas_Veteranos = acum_Cuotas_Categoria_Veteranos / cantidad_categoria_Veteranos
        else:
            promedio_cuotas_Veteranos = 0
    
    if cod_deportes[i] == "F" or cod_deportes[i] == "f":
        acum_Cuotas_Deporte_Futbol = acum_Cuotas_Deporte_Futbol + cuotas [i]
        
    elif cod_deportes[i] == "V" or cod_deportes[i] == "v":
        acum_Cuotas_Deporte_Voley = acum_Cuotas_Deporte_Voley + cuotas [i]
        
    elif cod_deportes[i] == "H" or cod_deportes[i] == "h":
        acum_Cuotas_Deporte_Handball = acum_Cuotas_Deporte_Handball + cuotas[i]
        
        
    
    os.system("cls")

print("**MUESTREO DE INSCRIPTOS**")
for i in range (cantidad_Inscriptos):
    print("ID INSCRIPTO: ", id_inscriptos [i], "| Nombre: ", nombres[i],"| Apellido: ", apellidos[i],"| Edad: ",edades[i])
    print("\nDATOS COLOCADOS | CODIGO DEPORTE: ", cod_deportes[i]," : ", deportes[i], "DIAS Y HORARIO: ",dias[i], horarrios_Practicas[i], " | CODIGO LOCALIDAD: ", cod_localidad[i], " : ", localidades[i])
    print("\nCUOTA A PAGAR: ", cuotas[i])
    print("===========================================================================================")