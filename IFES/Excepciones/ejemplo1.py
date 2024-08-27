import os
os.system("cls")


while True:
    print("-"*5,"Calculo de numeros","-"*5)
    os.system("cls")
    try:
        num1= int(input("Introduzca el numero 1: "))
        num2= int(input("Introduzca el numero 2: "))
        break
    except:
        input("ERROR[1] - UN VALOR INGRESADO NO ES UN NUMERO")
    
op = 0
while op < 1 or op > 4:
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicacion")
    print("4 - Division")
    op = int(input("Introduzca la operacion que desea realizar con los numeros: "))

if op == 1:
    print("Resultado: ", num1 +  num2)
elif op == 2:
    print("Resultado: ",  num1 -  num2)
elif op == 3:
    print("Resultado: ",  num1 *  num2)
else:
    try:
        print("Resultado: ",  num1 /  num2)
    except:
        print("ERROR [3] - NO SE PUEDE UN NUMERO ENTRE 0")
        num2 = int(input("Coloque otro valor para el numero 2: "))
