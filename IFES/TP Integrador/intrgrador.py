from tkinter import *
from tkinter import messagebox
from io import open

raiz = Tk()
raiz.resizable(True, True)
raiz.title("Confiteria lo de tito calderon")
raiz.config(bg="lightblue")

marco = Frame(raiz)
marco.pack(fill=None, expand=True)
marco.config(bg="pink", width=690, height=600)

def calcular():
    
    if Ver_EmpC.get()== 0 and valor_Cantidad_EC.get() > 0:
        valor_Cantidad_EC.set(0)
        messagebox.showerror("ERROR","Marque por lo menos una casilla para calcular")
    
    if Ver_EmpP.get() == 0 and valor_Cantidad_EP.get() > 0:
        valor_Cantidad_EP.set(0)
        messagebox.showerror("ERROR","Marque por lo menos una casilla para calcular")
    
    if Ver_Pizza.get() ==0 and valor_Cantidad_Pizza.get() > 0:
        valor_Cantidad_Pizza.set(0)
        messagebox.showerror("ERROR","Marque por lo menos una casilla para calcular")
        
    if Ver_Lomo.get() and valor_Cantidad_Lomo.get() > 0:
        valor_Cantidad_Lomo.set(0)
        messagebox.showerror("ERROR","Marque por lo menos una casilla para calcular")
    
    suma = 800 * valor_Cantidad_EC.get() + 800 * valor_Cantidad_EP.get() + 3000 * valor_Cantidad_Lomo.get() + 3500 * valor_Cantidad_Pizza.get()

    if Seleccion_Deliveri.get() == 1:
        
        if Ver_EmpC.get() != 0 and valor_Cantidad_EC.get() > 0:
            suma = suma + 500
        if Ver_EmpP.get() != 0 and valor_Cantidad_EP.get() > 0:
            suma = suma + 500
        if Ver_Pizza.get() != 0 and valor_Cantidad_Pizza.get() > 0:
            suma = suma + 500
        if Ver_Lomo.get() != 0 and valor_Cantidad_Lomo.get() > 0:
            suma = suma + 500
    else:
        suma = suma + 0
    
    if seleccion_Descuento.get() == 1:
        suma = suma - (suma*10/100)
    else:
        suma = suma * 1
    
    total.set(suma)


def reiniciar():
    
    respuesta_Reinicio = messagebox.askquestion("Reiniciar","¿Desea reiniciar los valores?")
    
    if respuesta_Reinicio == "yes":
        Seleccion_Deliveri.set(1)
        seleccion_Descuento.set(1)
        
        Ver_EmpC.set(0)
        Ver_EmpP.set(0)
        Ver_Pizza.set(0)
        Ver_Lomo.set(0)
        
        
        valor_Cantidad_EC.set(0)
        valor_Cantidad_EP.set(0)
        valor_Cantidad_Pizza.set(0)
        valor_Cantidad_Lomo.set(0)
        total.set(0)

def salir():
    respuesta_Salir = messagebox.askquestion("Salir","¿Desea salir de la aplicacion?")
    if respuesta_Salir == "yes":
        raiz.destroy()
        

def guardar_e_Imprimir():
    
    respuesta_Guardar_e_Imprimir = messagebox.askquestion("Guardar e imprimir","¿Desea guardar e imprimir los datos del pedido?")
    if respuesta_Guardar_e_Imprimir == "yes" and total.get() != 0:
        messagebox.showinfo("Guardado","Guardando e imprimiendo")
        archivo = open("IFES/TP Integrador/tickets/ticket.doc","w")

        archivo.write("Recibo")
        
        info_Nombre = nombre_Y_Apellido.get()
        info_Domicilio = domicilio.get()
        info_Nro_Telefono = numero_de_Telefono.get()
        
        archivo.write("Nombre y apellido: ",info_Nombre)
        archivo.write("Domicilio: ",info_Domicilio)
        archivo.write("Numero de telefono: ",info_Nro_Telefono)
        
        
        if valor_Cantidad_EC.get() > 0:
            cantidad_EC = valor_Cantidad_EC.get()
            archivo.write("Empanadas de Carne: ",cantidad_EC," Unidades")
        if valor_Cantidad_EP.get() > 0:
            cantidad_EP = valor_Cantidad_EP.get()
            archivo.write("Empanadas de Pollo: ",cantidad_EP," Unidades")
        if valor_Cantidad_Pizza.get() > 0:
            cantidad_Pizza = valor_Cantidad_Pizza.get()
            archivo.write("Empanadas de Carne: ",cantidad_Pizza," Unidades")
        if valor_Cantidad_Lomo.get() > 0:
            cantidad_Lomo = valor_Cantidad_Lomo.get()
            archivo.write("Empanadas de Carne: ",cantidad_Lomo," Unidades")
            
        if Seleccion_Deliveri.get() == 1:
            archivo.write("Con Deliveri: SI")
        else:
            archivo.write("Con Deliveri: No")
            
        if seleccion_Descuento.get() == 1:
            archivo.write("Con Descuento: SI")
        else:
            archivo.write("Con Descuento: NO")
        info_Total = total.get()
        
        archivo.write("TOTAL: ",info_Total)
    

# Texto de bienvenida
texto1 = Label(marco, text="Bienvenido!")
texto1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
texto1.config(bg="pink", fg="red", font=("Rockwell", 10, "bold"))

# Título de selección de comidas
texto2 = Label(marco, text="¿Qué comidas eligió el cliente?")
texto2.grid(row=2, column=0, sticky="w", padx=10, pady=10)
texto2.config(bg="pink", width=30, fg="black", font=("Rockwell", 10, "bold"), anchor="w")

texto_cantidad = Label(marco, text="Cantidades")
texto_cantidad.grid(row=2, column=1, padx=10, pady=10,sticky="w")
texto_cantidad.config(bg="pink", width=10, fg="black", font=("Rockwell", 10, "bold"), anchor="w")

# Comidas

valor_Cantidad_EP = IntVar()
valor_Cantidad_EC = IntVar()
valor_Cantidad_Pizza = IntVar()
valor_Cantidad_Lomo = IntVar()

Ver_EmpC = IntVar()
Ver_EmpP = IntVar()
Ver_Pizza = IntVar()
Ver_Lomo = IntVar()

total= IntVar()

nombre_Y_Apellido = StringVar()
numero_de_Telefono = IntVar()
domicilio = StringVar()

chkEmp_Pollo = Checkbutton(marco, text="Empanada de pollo", variable=Ver_EmpP, onvalue=1, offvalue=0)
chkEmp_Pollo.grid(row=3, column=0, sticky="w", padx=10, pady=10)
chkEmp_Pollo.config(fg="black", bg="pink", width=16, font=("Rockwell", 10), anchor="w")

texto_Cantidad_Pollo = Entry(marco,textvariable=valor_Cantidad_EP)
texto_Cantidad_Pollo.grid(row=3, column=1, sticky="w", padx=10, pady=10)
texto_Cantidad_Pollo.config(bg="white", width=4)

chkEmp_Carne = Checkbutton(marco, text="Empanada de Carne", variable=Ver_EmpC, onvalue=1, offvalue=0)
chkEmp_Carne.grid(row=4, column=0, sticky="w", padx=10, pady=10)
chkEmp_Carne.config(fg="black", bg="pink", width=17, font=("Rockwell", 10), anchor="w")

texto_Cantidad_Carne = Entry(marco,textvariable=valor_Cantidad_EC)
texto_Cantidad_Carne.grid(row=4, column=1, sticky="w", padx=10, pady=10)
texto_Cantidad_Carne.config(bg="white", width=4)

chk_Pizza = Checkbutton(marco, text="Pizza", variable=Ver_Pizza, onvalue=1, offvalue=0)
chk_Pizza.grid(row=5, column=0, sticky="w", padx=10, pady=10)
chk_Pizza.config(fg="black", bg="pink", width=16, font=("Rockwell", 10), anchor="w")

texto_Cantidad_Pizza = Entry(marco,textvariable=valor_Cantidad_Pizza)
texto_Cantidad_Pizza.grid(row=5, column=1, sticky="w", padx=10, pady=10)
texto_Cantidad_Pizza.config(bg="white", width=4)

chk_Lomo = Checkbutton(marco, text="Lomo", variable=Ver_Lomo, onvalue=1, offvalue=0)
chk_Lomo.grid(row=6, column=0, sticky="w", padx=10, pady=10)
chk_Lomo.config(fg="black", bg="pink", width=16, font=("Rockwell", 10), anchor="w")

texto_Cantidad_Lomo = Entry(marco,textvariable=valor_Cantidad_Lomo)
texto_Cantidad_Lomo.grid(row=6, column=1, sticky="w", padx=10, pady=10)
texto_Cantidad_Lomo.config(bg="white", width=4)

boton_Calcular = Button(marco, text="CALCULAR", command=lambda:calcular())
boton_Calcular.grid(row=11, column=0, padx=5, pady=5, sticky="w")
boton_Calcular.config(bg="lightgray", fg="green", width=15, font=("Arial", 12, "bold"))

boton_Reiniciar = Button(marco, text="REINICIAR", command=lambda:reiniciar())
boton_Reiniciar.grid(row=11, column=1, padx=5, pady=5, sticky="w")
boton_Reiniciar.config(bg="lightgray", fg="black", width=15, font=("Arial", 12, "bold"))

boton_Guardar = Button(marco, text="GUARDAR E IMPRIMIR", command=lambda:guardar_e_Imprimir())
boton_Guardar.grid(row=6, column=2, padx=5, pady=5,columnspan=2)
boton_Guardar.config(bg="lightgray", fg="blue", width=20, font=("Arial", 12, "bold", "italic"))

boton_Salir = Button(marco, text="SALIR", command=lambda:salir())
boton_Salir.grid(row=7, column=2, padx=5, pady=5,columnspan=2)
boton_Salir.config(bg="lightgray", fg="red", width=20, font=("Arial", 12, "bold", "italic"))


texto4 = Label(marco, text="Datos Del Cliente")
texto4.grid(row=2, column=2, padx=10, pady=10,sticky="w")
texto4.config(bg="pink", width=14, fg="black", font=("Rockwell", 10,"bold"), anchor="w")

texto_Nombre = Label(marco, text="Nombre y Apellido")
texto_Nombre.grid(row=3, column=2, padx=10, pady=10)
texto_Nombre.config(bg="pink", width=15, fg="black", font=("Rockwell", 10), anchor="w")

texto_Nombre_Apellido = Entry(marco, textvariable= nombre_Y_Apellido)
texto_Nombre_Apellido.grid(row=3, column=3, sticky="w", padx=10, pady=10)
texto_Nombre_Apellido.config(bg="white", width=15)

texto_Numero = Label(marco, text="Número de teléfono")
texto_Numero.grid(row=4, column=2, padx=10, pady=10)
texto_Numero.config(bg="pink", width=16, fg="black", font=("Rockwell", 10), anchor="w")

texto_Numero_Telefono = Entry(marco, textvariable= numero_de_Telefono)
texto_Numero_Telefono.grid(row=4, column=3, sticky="w", padx=10, pady=10)
texto_Numero_Telefono.config(bg="white", width=15)

texto_Domicilio = Label(marco, text="Domicilio")
texto_Domicilio.grid(row=5, column=2, padx=10,)
texto_Domicilio.config(bg="pink", width=15, fg="black", font=("Rockwell", 10), anchor="w")

texto_Domicilio = Entry(marco, textvariable=domicilio)
texto_Domicilio.grid(row=5, column=3, sticky="w", padx=10, pady=10)
texto_Domicilio.config(bg="white", width=15)

texto3 = Label(marco, text="Tipo de retiro")
texto3.grid(row=7, column=0, padx=10, pady=10,sticky="w")
texto3.config(bg="pink", width=11, fg="black", font=("Rockwell", 10, "bold"), anchor="w")

Seleccion_Deliveri = IntVar(value=1)

Rbutton_Delivery = Radiobutton(marco, text="Con Delivery", value=1, variable=Seleccion_Deliveri)
Rbutton_Delivery.grid(row=8, column=0, padx=10, pady=10, sticky="w")
Rbutton_Delivery.config(bg="pink")

Rbutton_Local = Radiobutton(marco, text="Retiro en el local", value=2, variable=Seleccion_Deliveri)
Rbutton_Local.grid(row=9, column=0, padx=10, pady=10, sticky="w")
Rbutton_Local.config(bg="pink")

texto5 = Label(marco, text="¿Hay dia de descuento?")
texto5.grid(row=7, column=1, padx=2, pady=10,sticky="w")
texto5.config(bg="pink", width=20, fg="black", font=("Rockwell", 10, "bold"), anchor="w")

seleccion_Descuento = IntVar(value=1)

Rbutton_Si = Radiobutton(marco, text="Si", value=1, variable=seleccion_Descuento)
Rbutton_Si.grid(row=8, column=1, padx=10, pady=10, sticky="w")
Rbutton_Si.config(bg="pink")

Rbutton_No = Radiobutton(marco, text="No", value=2, variable=seleccion_Descuento)
Rbutton_No.grid(row=9, column=1, padx=10, pady=10, sticky="w")
Rbutton_No.config(bg="pink")



texto_Total = Label(marco, text="TOTAL")
texto_Total.grid(row=12, column=0, padx=10,pady=10,sticky="w")
texto_Total.config(bg="pink", width=15, fg="black", font=("Rockwell", 10), anchor="w")

texto_Total = Entry(marco,textvariable= total)
texto_Total.grid(row=12, column=1, sticky="w", padx=10, pady=10)
texto_Total.config(bg="white", width=15)


raiz.mainloop()