import os
os.system("cls")

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
cod_Categoria = input("Ingrese la categoria del trabajador: ")

diccionario_Categorias = {"A":"Vendedor", "B":"Administrativo", "C":"Cajero"}
diccionario_Sueldo = {"A":750000, "B":820000, "C":780000}

if cod_Categoria != "A" and cod_Categoria != "B" and cod_Categoria != "C":
    print ("Ingrese una categoria valida")
else:
    if cod_Categoria == "A":
        categoria_Empleado = diccionario_Categorias ["A"]
        sueldo_Empleado = diccionario_Sueldo["A"]
    
    elif cod_Categoria == "B":
        categoria_Empleado = diccionario_Categorias["B"]
        sueldo_Empleado = diccionario_Sueldo["B"]
    
    elif cod_Categoria == "C":
        categoria_Empleado = diccionario_Categorias["C"]
        sueldo_Empleado = diccionario_Sueldo["C"]
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#        
    print("El empleado", nombre, apellido, "de categoria", cod_Categoria, "tabaja en el puesto de", categoria_Empleado, "y tiene un salario de", sueldo_Empleado)