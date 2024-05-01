import os
os.system("cls")

numero_Uno = int(input("Ingrese el primer numero: "))
numero_Dos = int(input("Ingrese el segundo numero: "))

suma_Numeros = numero_Uno + numero_Dos

if suma_Numeros >= 100:
        print ("La suma es mayor que 100, se imprime", numero_Uno)
else:
        print ("La suma es menor que 100, se imprime", numero_Dos)
