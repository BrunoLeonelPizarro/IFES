import os
os.system("cls")

def desicion_Dias_Vacaciones (a):
    if a <= 7:
        dias_de_Vcaciones = "14"
    elif a <= 14:
        dias_de_Vcaciones = "21"
    elif a <= 21:
        dias_de_Vcaciones = "28"
    else:
        dias_de_Vcaciones = "35"
    return dias_de_Vcaciones

def descuento_Vacaciones (a,b):
    descuento_Salario = (a*b)/100
    return descuento_Salario

def porcentaje_de_plus(a,b):
    porcentaje = (a * 100) / b
    return porcentaje

def salario_Con_Plus (a):
    nuevo_Salario = descuento_Vacaciones(sueldo, a) + sueldo
    return nuevo_Salario

apellido = input("Ingrese el apellido: ")
sueldo = int(input("Ingrese el salario: "))
antiguedad = int(input("Ingrese la antiguedad: "))

diccionario_Dias_Vacaciones = {"14 dias":salario_Con_Plus(2) , "21 dias":salario_Con_Plus(3), "28 dias":salario_Con_Plus(4), "otro":salario_Con_Plus(6)}

if antiguedad <= 7:
    salario_Vacaciones = diccionario_Dias_Vacaciones["14 dias"]
elif antiguedad <= 14:
    salario_Vacaciones = diccionario_Dias_Vacaciones["21 dias"]
elif antiguedad <= 21:
    salario_Vacaciones = diccionario_Dias_Vacaciones["28 dias"]
else:
    salario_Vacaciones = diccionario_Dias_Vacaciones["otro"]

print("El trabajador de apellido", apellido, "con", antiguedad, "años de antiguedad va a recibir", desicion_Dias_Vacaciones(antiguedad), "dias de vacaciones con un plus vacacional del", porcentaje_de_plus(salario_Vacaciones - sueldo, sueldo),"% y asi teniendo un salario de:", salario_Vacaciones )