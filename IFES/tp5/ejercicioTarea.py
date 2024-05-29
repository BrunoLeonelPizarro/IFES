import os
os.system("cls")

apellidos = []
nombres = []
edades = []
cod_deportes = []
deporte = []
cod_localidad = []
localidades = []

cuotas = []

dias = []
horarrios_Practicas = []
categorias = []

cod_deportes = []
deportes = []


cantidad_Inscriptos = 3
id_inscriptos = []
id_inscripto = 0


for i in range (cantidad_Inscriptos):
    id_inscripto = id_inscripto + 1
    id_inscriptos.append(id_inscripto)
    print ("Id N°: ", id_inscriptos [i] )
    apellidos.append(input("Ingrese su apellido: ").capitalize())
    nombres.append(input("Ingrese su nombre: ").upper())
    edad = int(input("Ingrese su edad: "))
    while edad < 12 or edad > 50:
        edad = int(input("ERROR | Ingrese una edad entre 12 y 50 años: "))
        os.system("cls")
    edades.append(edad)
    if edad <= 15:
        dias.append("Viernes")
        horarrios_Practicas.append("17:00")
        categorias.append("Infantil")
    elif edad <= 18:
        dias.append("Viernes")
        horarrios_Practicas.append("19:00")
        categorias.append("Juveniles")
    elif edad <= 24:
        dias.append("Viernes")
        horarrios_Practicas.append("21:00")
        categorias.append("Adultos")
    elif edad <= 40:
        dias.append("Sabado")
        horarrios_Practicas.append("14:00")
        categorias.append("Mayores")
    else:
        dias.append("Sabado")
        horarrios_Practicas.append("16:00")
        categorias.append("Veteranos")

    codigo_deporte = input("Ingrese un codigo de deporte (F: (FUTBOL) | V: (VOLEY) | H: (HANDBALL)): ")
    codigo_deporte.capitalize()
    while codigo_deporte != "F" and codigo_deporte != "V" and codigo_deporte != "H":
        codigo_deporte = input("Ingrese un codigo de deporte valido (F: (FUTBOL) | V: (VOLEY) | H: (HANDBALL)) : ")
        os.system("cls")
    cod_deportes.append(codigo_deporte)
    
    if codigo_deporte == "F":
        deportes.append("Futbol")
    elif codigo_deporte == "V":
        deportes.append("Voley")
    elif codigo_deporte == "H":
        deportes.append("Handball")
    
    codigo_localidad = input("iNGRESE UN CODIGO DE LOCALIDAD (C: CIPOLETTI | N: NEUQUEN | P: PLOTTIER): ")
    codigo_localidad.capitalize()
    while codigo_localidad != "C" and codigo_localidad != "N" and codigo_localidad != "P":
        codigo_localidad = input("Ingrese un codigo de lOCALIDAD valido (C: CIPOLETTI | N: NEUQUEN | P: PLOTTIER): ")
        os.system("cls")
    cod_localidad.append(codigo_localidad)
    if codigo_localidad == "C":
        localidades.append("Cipolletti")
    elif codigo_localidad == "N":
        localidades.append("Neuquen")
    elif codigo_localidad == "P":
        localidades.append("Plottier")
    
    valor_cuota = int(input("Ingrese el valor de la cuota: "))
    while valor_cuota < 0:
        valor_cuota = int(input("ERROR VALOR CUOTA | Ingrese un valor mayor a 0: "))
    cuotas.append(valor_cuota)
    os.system("cls")
    
for i in range (cantidad_Inscriptos):
    print("**MUESTREO DE INSCRIPTOS**")
    print("ID INSCRIPTO: ", id_inscriptos [i], "| Nombre: ", nombres[i],"| Apellido: ", apellidos[i],"| Edad: ",edades[i])
    print("DATOS COLOCADOS | CODIGO DEPORTE: ", cod_deportes[i]," : ", deportes[i], "DIAS Y HORARIO: ",dias[i], horarrios_Practicas[i], " | CODIGO LOCALIDAD: ", cod_localidad[i], " : ", localidades[i])
    print("CUOTA A PAGAR: ", cuotas[i])
    print("===========================================================================================")