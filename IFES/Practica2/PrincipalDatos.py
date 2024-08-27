import os
import re
from io import open
import sqlite3
os.system("cls")

misContactos = {}

def funcion_AgregarDatos():
    ok = False
    while ok == False:
        os.system("cls")
        print("-"*10,"Agregar nuevo contacto","-"*10)
        print("-"*40)
        nombre = input("Introduzca el nombre del contacto: ")
        Numero = input("Ontroduzca el numero de telefono: ")
        SiNo = input("¿Quiere confirmar la carga del contacto?[Si / s | No / n]: ")
        if SiNo == "s":
            if nombre.isalpha() and Numero.isdigit():
                miCursor.execute("INSERT INTO CONTACTOS VALUES ('%s',%s)" %(nombre, Numero))
                miConexion.commit()
                ok = True
                input ("\nContacto Agregado - Presione enter para continuar: ")
            else:
                input("ERROR - Datos no validos - Presione enter para continuar")
        else:
            ok = True

def funcion_ModificarDatos():
    os.system("cls")
    print("-"*10,"Modificar contacto","-"*10)
    print("-"*40)
    nombre = input("Ingrese el nombre del contacto: ")
    miCursor.execute("SELECT * FROM CONTACTOS WHERE NOMBRE = '%s'" %nombre)
    datos = miCursor.fetchall()
    if datos != None:
        print("Telefono del contacto: ",datos[1])
        numero = input("Introduzca el nuevo numero de telefono: ")
        siNo = input("Desea modificar el numero de telefono?[Si / s | No / n]: ")
        if siNo == "s":
            if numero.isdigit():
                miCursor.execute("UPDATE CONTACTOS SET TELEFONO = %s WHERE NOMBRE = '%s'" %(numero,nombre))
                miConexion.commit()
                input("Contacto actualizado - Presione enter para continuar: ")
            else:
                input("El dato del telefono es erroneo - Oprima enter para continuar: ")
        else:
            input("Modificacion no confirmada - Oprima enter para continuar: ")
    else:
        input("ERROR - El contacto colocado no existe - Presione enter para continuar")

def funcion_EliminarDatos():
    os.system("cls")
    print(("-"*10),"Eliminar contacto",("-"*10))
    print(("-")*40)
    nombre = input("Introduzca el nombre del contacto: ")
    miCursor.execute("SELECT * FROM CONTACTOS WHERE NOMBRE = '%s'" %nombre)
    datos = miCursor.fetchone()
    if datos != None:
        print("El telefono del contacto introducido es: ",datos[1])
        siNo = input("Desea eliminar el contacto introducido? [Si (s) | No (n) ]: ")
        if siNo == "s":
            miCursor.execute("DELETE FROM CONTACTOS WHERE NOMBRE = '%s'" %nombre)
            miConexion.commit()
            input("Contacto eliminado - Oprima enter para salir: ")
        else:
            input("Se cancelo la eliminacion. Oprima enter para salir: ")
    else:
        input("Error - No existe el contacto escrito - Oprima enter para salir: ")

def funcion_BuscarDatos():
    os.system("cls")
    print(("-"*10),"Buscar datos",("-"*10))
    print(("-")*40)
    texto = input("Introduzca el texto de busqueda: ")
    texto =texto.strip()+"%"
    print ("\n",("-"*10),"Listar contactos",("-"*10))
    print(("-"*40))
    print("     Nombre          Numero  ")
    print(("-"*40))
    miCursor.execute("SELECT * FROM CONTACTOS WHERE NOMBRE LIKE '%s'" %texto)
    datos = miCursor.fetchall()
    for dato in datos:
        print((" "*6),dato[0],(" "*20), dato[1])
    input("\n Oprima enter para continuar: ")

def funcion_MostrarDatos():
    os.system("cls")
    print(("-"*10),"Lista de contactos",("-"*10))
    print(("-"*40))
    datos = miCursor.execute("SELECT * FROM CONTACTOS")
    datos.fetchall
    print("     Nombre          Numero      ")
    print(("-"*40))
    for dato in datos:
        print((" "*6),dato[0],((" ")*6),dato[1])
    input("\nOprima enter para salir: ")

def funcion_ExportarDatos():
    archivo = open("IFES/Practica2/BDP/documento.txt", "w")
    datos = miCursor.execute("SELECT * FROM CONTACTOS")
    datos.fetchall
    for dato in datos:
        linea = dato[0]+(" "*20)+str(dato[1])+'\n'
        archivo.write(linea)
    archivo.close
    os.system("cls")

miConexion = sqlite3.connect("IFES/Practica2/BDP/BasePreactica")
miCursor = miConexion.cursor()

op = 0
while op != 7:
    os.system("cls")
    print("-"*10,'AGENDA DE CONTACTOS','-'*10)
    print("-"*46)
    print("1 - Agregar un nuevo contacto",
        "\n2 - Listar agenda",
        "\n3 - Modificar contacto",
        "\n4 - Eliminar contacto",
        "\n5 - Busqueda fina",
        "\n6 - Exportar datos",
        "\n 7 - Salir")
    op = int(input("Elija una opcion: "))
    if op == 1:
        funcion_AgregarDatos()
    elif op == 2:
        funcion_MostrarDatos()
    elif op == 3:
        funcion_ModificarDatos()
    elif op == 4:
        funcion_EliminarDatos()
    elif op == 5:
        funcion_BuscarDatos()
    elif op == 6:
        funcion_ExportarDatos()
    elif op > 7 or op < 1:
        input("Opcion Invalida")
miConexion.close()