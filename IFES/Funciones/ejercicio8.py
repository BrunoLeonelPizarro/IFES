import os
os.system ("cls")

def Calc_Temp_media(a,b):
    temperatura_Med = (a + b) / 2
    return temperatura_Med


temperatura_Minima = int(input("Ingrese la temperatura minima: "))
temperatura_Maxima = int(input("Ingrese la temperatura maxima: "))

temperatura_Media = Calc_Temp_media (temperatura_Maxima, temperatura_Minima)

print("\nLa temperatura media del dia es de:", temperatura_Media)