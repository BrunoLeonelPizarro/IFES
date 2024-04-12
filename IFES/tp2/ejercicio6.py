import os
os.system("cls")

def calc_Horas_Normales (a):
    valor_Horas_Normales = a * 1500
    return valor_Horas_Normales

def calc_Horas_Extra (a,b):
    valor_Horas_Extra = (((a*50)/100) + a) * b
    return valor_Horas_Extra



print("Ingrese los datos de la persona: ")
nombre = input("Ingrese el nombre: ")
apellido = input ("Ingrese el apellido: ")
legajo = int (input("Ingrese el legajo: "))

horas_Normales = int(input("\nIngrese la cantidad de horas normales: "))
horas_Extra = int(input("Ingrese las horas extra: "))

total_Horas_Normales = calc_Horas_Normales (horas_Normales)
total_Horas_Extra = calc_Horas_Extra (horas_Normales, horas_Extra)
total_Horas = total_Horas_Normales + total_Horas_Extra

print ("\nla persona:", nombre, apellido, "Con legajo:", legajo)
print("Treabajo ", horas_Normales, "horas normales y", horas_Extra, "horas extra.")
print ("Por horas normales gano:", total_Horas_Normales,"$ y por horas extra gano: ", total_Horas_Extra,"$")
print("Gano  un total de", total_Horas)