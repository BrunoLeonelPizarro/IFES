import os
os.system("cls")

def funcion_contador (a):
    resultado_Funcion_contador = 0
    resultado_Funcion_contador = a + 1
    return resultado_Funcion_contador

def funcion_acumulador (a):
    resultado_Funcion_acumulador = 0
    resultado_Funcion_acumulador = resultado_Funcion_acumulador + a[i]
    return resultado_Funcion_acumulador
    
def funcion_promedio (a,b):
    resultado_Funcion_promedio = 0
    if a == 0:
        resultado_Funcion_promedio = 0
    else:
        resultado_Funcion_promedio  = b / a
    return resultado_Funcion_promedio

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
cantidad_cuotas = 0

acum_Cuotas_Categoria_Infantiles = 0
acum_Cuotas_Categoria_Juveniles = 0
acum_Cuotas_Categoria_Adultos = 0
acum_Cuotas_Categoria_Mayores = 0
acum_Cuotas_Categoria_Veteranos = 0
acum_Cuotas_Deporte_Futbol = 0
acum_Cuotas_Deporte_Voley = 0
acum_Cuotas_Deporte_Handball = 0
acum_Promedio_Cuotas = 0

promedio_cuotas_Infantiles = 0
promedio_cuotas_Juveniles = 0
promedio_cuotas_Adultos = 0
promedio_cuotas_Mayores = 0
promedio_cuotas_Veteranos = 0
promedio_Cuotas_deporte_Futbol = 0
promedio_Cuotas_deporte_Voley = 0
promedio_Cuotas_deporte_Handball = 0
promedio_cuotas_Total = 0

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


cantidad_Inscriptos = 2
id_inscriptos = []
id_inscripto = 0


for i in range (cantidad_Inscriptos):
    id_inscriptos.append(funcion_contador(i))  
    print ("Id N°: ", id_inscriptos [i] )
    apellidos.insert(i,(input("Ingrese su apellido: ")).capitalize())
    nombres.insert(i,(input("Ingrese su nombre: ")).upper())
    edades.insert(i,(int(input("Ingrese su edad: "))))
    while edades[i] < 12 or edades[i] > 50:
        os.system("cls")
        edades.insert(i,(int(input("ERROR EDAD | Ingrese una edad entre 12 y 50 años: "))))
        os.system("cls")
    if edades[i] <= 15:
        dias.append("Viernes")
        horarrios_Practicas.append("17:00")
        categorias.append("Infantil")
        cantidad_categoria_Infantiles = funcion_contador(cantidad_categoria_Infantiles)
    elif edades[i] <= 18:
        dias.append("Viernes")
        horarrios_Practicas.append("19:00")
        categorias.append("Juveniles")
        cantidad_categoria_Juveniles = funcion_contador(cantidad_categoria_Juveniles)
    elif edades[i] <= 24:
        dias.append("Viernes")
        horarrios_Practicas.append("21:00")
        categorias.append("Adultos")
        cantidad_categoria_Adultos = funcion_contador(cantidad_categoria_Adultos)
    elif edades[i] <= 40:
        dias.append("Sabado")
        horarrios_Practicas.append("14:00")
        categorias.append("Mayores")
        cantidad_categoria_Mayores = funcion_contador(cantidad_categoria_Mayores)
    else:
        dias.append("Sabado")
        horarrios_Practicas.append("16:00")
        categorias.append("Veteranos")
        cantidad_categoria_Veteranos = funcion_contador(cantidad_categoria_Veteranos)

    cod_deportes.insert(i,(input("Ingrese un codigo de deporte (F: (FUTBOL) | V: (VOLEY) | H: (HANDBALL)): ")).upper())
    while cod_deportes[i] != "F" and cod_deportes[i] != "V" and cod_deportes[i] != "H":
        os.system("cls")
        cod_deportes.insert(i,(input("ERROR CODIGO DEPORTE | Ingrese un codigo de deporte valido (F: (FUTBOL) | V: (VOLEY) | H: (HANDBALL)) : ")).upper())
        os.system("cls")
    
    if cod_deportes[i] == "F":
        deportes.append("Futbol")
        cantidad_deporte_Futbol = funcion_contador(cantidad_deporte_Futbol)
    elif cod_deportes[i] == "V":
        deportes.append("Voley")
        cantidad_deporte_Voley = funcion_contador(cantidad_deporte_Voley)
    elif cod_deportes[i] == "H":
        deportes.append("Handball")
        cantidad_deporte_Handball = funcion_contador(cantidad_deporte_Handball)
    
    cod_localidad.insert(i,(input("INGRESE UN CODIGO DE LOCALIDAD (C: CIPOLETTI | N: NEUQUEN | P: PLOTTIER): ")).upper())
    while cod_localidad[i] != "C" and cod_localidad[i] != "N" and cod_localidad[i] != "P":
        os.system("cls")
        cod_localidad.insert(i,(input("Ingrese un codigo de lOCALIDAD valido (C: CIPOLETTI | N: NEUQUEN | P: PLOTTIER): ")).upper())
        os.system("cls")
    
    if cod_localidad[i] == "C":
        localidades.append("Cipolletti")
        cantidad_localidad_de_Cipolletti = funcion_contador(cantidad_localidad_de_Cipolletti)
    elif cod_localidad[i] == "N":
        localidades.append("Neuquen")
        cantidad_localidad_de_Neuquen = funcion_contador(cantidad_localidad_de_Neuquen)
    elif cod_localidad[i] == "P":
        localidades.append("Plottier")
        cantidad_localidad_de_Plottier = funcion_contador(cantidad_localidad_de_Plottier)
    
    cuotas.insert(i,(int(input("Ingrese el valor de la cuota: "))))
    while cuotas[i] <= 0:
        os.system("cls")
        cuotas.insert(i,(int(input("ERROR VALOR CUOTA | Ingrese un valor mayor a 0: "))))
        os.system("cls")
    cantidad_cuotas = funcion_contador(cantidad_cuotas)
        
    if categorias [i] == "Infantil":
        acum_Cuotas_Categoria_Infantiles = funcion_acumulador(cuotas)
        
    elif categorias[i] == "Juveniles":
        acum_Cuotas_Categoria_Juveniles = funcion_acumulador(cuotas)
        
    elif categorias[i]== "Adultos":
        acum_Cuotas_Categoria_Adultos = funcion_acumulador(cuotas)
        
    elif categorias [i] == "Mayores":
        acum_Cuotas_Categoria_Mayores = funcion_acumulador(cuotas)
        
    elif categorias [i] == "Veteranos":
        acum_Cuotas_Categoria_Veteranos = funcion_acumulador (cuotas)
        
    if deportes [i] == "Futbol":
        acum_Cuotas_Deporte_Futbol = funcion_acumulador (cuotas)
        promedio_Cuotas_deporte_Futbol = funcion_promedio (cantidad_deporte_Futbol, acum_Cuotas_Deporte_Futbol)
    elif deportes [i] == "Voley":
        acum_Cuotas_Deporte_Voley = funcion_acumulador (cuotas)
        promedio_Cuotas_deporte_Voley = funcion_promedio (cantidad_deporte_Futbol, acum_Cuotas_Deporte_Voley)
    elif deportes [i] == "Handball":
        acum_Cuotas_Deporte_Handball = funcion_acumulador(cuotas)
        promedio_Cuotas_deporte_Handball = funcion_promedio (cantidad_deporte_Handball, acum_Cuotas_Deporte_Handball)

    acum_Cuotas = acum_Cuotas_Deporte_Voley + acum_Cuotas_Deporte_Futbol + acum_Cuotas_Deporte_Handball
    promedio_cuotas_Total = funcion_promedio (cantidad_cuotas, acum_Cuotas)
    
    if deportes [i] == "Futbol" and categorias [i] == "Veteranos":
        cantidad_futbol_veteranos = funcion_contador (cantidad_futbol_veteranos)
    else:
        cantidad_futbol_veteranos = cantidad_futbol_veteranos + 0
    
    os.system("cls")

print("**MUESTREO DE INSCRIPTOS**")
for i in range (cantidad_Inscriptos):
    print("ID INSCRIPTO: ", id_inscriptos [i], "| Nombre: ", nombres[i],"| Apellido: ", apellidos[i],"| Edad: ",edades[i])
    print("\nDATOS COLOCADOS | CODIGO DEPORTE: ", cod_deportes[i]," : ", deportes[i], "DIAS Y HORARIO: ",dias[i], horarrios_Practicas[i], " | CODIGO LOCALIDAD: ", cod_localidad[i], " : ", localidades[i])
    print("\nCUOTA A PAGAR: ", cuotas[i])
    print("===========================================================================================")
    input("Presione enter para continuar")

print("\n**MUESTREO FINAL**")
print("CANTIDAD DE ALUMNOS POR CATEGORIA | Infantiles: ",cantidad_categoria_Infantiles, "| Juveniles: ", cantidad_categoria_Juveniles, "| Adultos: ",cantidad_categoria_Adultos, "| Mayores: ", cantidad_categoria_Mayores, "| Veteranos: ", cantidad_categoria_Veteranos)
print ("CANTIDAD DE ALUMNOS POR DEPORTE: | Futbol: ",cantidad_deporte_Futbol," | Voley: ",cantidad_deporte_Voley," | Handball: ", cantidad_deporte_Handball)
print("CANTIDAD DE ALUMNOS POR LOCALIDAD: | Cipolletti: ", cantidad_localidad_de_Cipolletti," | Neuquen: ", cantidad_localidad_de_Neuquen," | Plottier: ",cantidad_localidad_de_Plottier)
print("CANTIDAD DE ALUMNOS QUE HACEN FUTBOL Y PERTENECEN A LA CATEGORIA DE VETERANOS: ",cantidad_futbol_veteranos)
print ("PROMEDIO DE CUOTAS POR DEPORTE: | Futbol: ",promedio_Cuotas_deporte_Futbol," | Voley: ",promedio_Cuotas_deporte_Voley," | Handball: ",promedio_Cuotas_deporte_Handball)
print("PROMEDIO DE TODAS LAS CUOTAS: ",promedio_cuotas_Total)