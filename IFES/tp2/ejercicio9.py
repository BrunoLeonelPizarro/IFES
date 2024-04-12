import os
os.system("cls")

def Segundos_A_Minutos(a):
    minutos = (a // 60) % 60
    return minutos

def minutos_A_Horas (a):
    horas = (a // 60) // 60
    return horas

def red_segundos (a):
    seg = a % 60
    return seg

segundos = int(input("Ingresar la cantidad de segundos: "))
min = Segundos_A_Minutos(segundos)
hora = minutos_A_Horas (segundos)
segundos_redondeado =red_segundos(segundos)

print(segundos, "segundos equivale a", hora, "Horas", min, "minutos y", segundos_redondeado, "segundos")