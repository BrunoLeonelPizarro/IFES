from tkinter import *
def calcular():
    suma = valor1.get() + valor2.get() + valor3.get()
    
    if flete.get() == 1:
        suma= suma*1.1
    if garantia.get() == 1:
        suma=suma*1.1
    total.set(suma)
    
    
def nuevo():
    valor1.set(0)
    valor2.set(0)
    valor3.set(0)
    total.set(0)
    flete.set(0)
    garantia.set(0)

def salir():
    raiz.destroy()

def creacion_Etiqueta(marco_Entrada, texto_A_colocar):
    etiqueta = Label(marco_Entrada, text=texto_A_colocar)
    return etiqueta

def grid_Etiqueta(etiqueta_Entrada, row_Entrada, column_Entrada, sticky_Entrada, pady_Entrada, padx_Entrada):
    etiqueta_Entrada.grid(row=row_Entrada, column=column_Entrada, sticky=sticky_Entrada, pady=pady_Entrada, padx=padx_Entrada)

def configurar_Etiqueta(etiqueta_Entrada, bg_Entrada, width_Entrada, tipo_Fuente, tamanio_Fuente, negrita_Entrada,anchor_Entrada):
    etiqueta_Entrada.config(bg=bg_Entrada, width=width_Entrada, font=(tipo_Fuente, tamanio_Fuente, negrita_Entrada),anchor= anchor_Entrada)

def creacion_Texto(marco_Entrada, texto_Variable_Entrada):
    texto = Entry(marco_Entrada,textvariable = texto_Variable_Entrada)
    return texto

def grid_Texto(texto_Entrada,row_Entrada,column_Entrada,sticky_Entrada, pady_Entrada, padx_Entrada):
    texto_Entrada.grid(row=row_Entrada, column=column_Entrada, sticky=sticky_Entrada, pady=pady_Entrada, padx=padx_Entrada)

def configuracion_Texto(entrada_Texto, bg_Entrada, fuente_Entrada, tamanio_Fuente, negrita_Entrada, italic_Entrada):
    entrada_Texto.config(bg=bg_Entrada, font=(fuente_Entrada, tamanio_Fuente, negrita_Entrada, italic_Entrada))

def creacion_boton(marco_Entrada, texto_Boton,asignar_Comando):
    boton = Button(marco_Entrada, text=texto_Boton, command = asignar_Comando)
    return boton

def configuracion_Grid_Boton(boton_Entrada, row_Entrada, column_Entrada, pady_Entrada, padx_Entrada, columnSpan_Entrada):
    boton_Entrada.grid(row=row_Entrada, column=column_Entrada, pady=pady_Entrada, padx=padx_Entrada, columnspan=columnSpan_Entrada)
    
def configuracion_De_Boton(boton_Entrada, bg_Entrada, width_Entrada, fuente_Entrada, tamanio_Fuente, negrita_Entrada, italic_Entrada):
    boton_Entrada.config(bg=bg_Entrada, width=width_Entrada, font=(fuente_Entrada, tamanio_Fuente, negrita_Entrada, italic_Entrada))

raiz = Tk()
raiz.resizable(True, True)
raiz.title("**CALCULO DE COMPRAS**")
raiz.config(cursor="star", bg="gray")
suma = 0

valor1 = IntVar()
valor2 = IntVar()
valor3 = IntVar()
total= IntVar()

raiz.iconbitmap('IFES/Interfaz Grafica/Iconos/compu.ico')

marco = Frame(raiz, bg="lightgray", width=650, height=350)
marco.pack(fill="none", expand=True)
marco.config(bg="lightblue", width=650, height=350)

etiqueta1 = creacion_Etiqueta(marco, "**Calculo de compras**")
grid_Etiqueta(etiqueta1, 0,0,"w",10,10)
configurar_Etiqueta(etiqueta1,"white",30,"Arial",10,"bold",None)

etiqueta2 = creacion_Etiqueta(marco, "Ingresa valor N°1")
grid_Etiqueta(etiqueta2,1,0,"w",10,10)
configurar_Etiqueta(etiqueta2,"white",20,"Arial",10,"bold","w")

texto1 = creacion_Texto(marco,valor1)
grid_Texto(texto1,1,1,"w",10,10)


etiqueta3 = creacion_Etiqueta(marco, "Ingrese valor N°2")
grid_Etiqueta(etiqueta3,3,0,"w",10,10)
configurar_Etiqueta(etiqueta3,"white",20,"Arial",10,"bold","w")

texto2 = creacion_Texto (marco,valor2)
grid_Texto(texto2,3,1,"w",10,10)


etiqueta4 = creacion_Etiqueta(marco, "Ingrese valor N°3")
grid_Etiqueta(etiqueta4,4,0,"w",10,10)
configurar_Etiqueta(etiqueta4,"white",20,"Arial",10,"bold","w")
texto3 = creacion_Texto (marco,valor3)
grid_Texto(texto3,4,1,"w",10,10)

boton1 = creacion_boton(marco,"CONFIRMAR",lambda:calcular())
configuracion_Grid_Boton(boton1,5,0,10,10,None)
configuracion_De_Boton(boton1,"White",20,"Arial",10,"bold","italic")

boton2 = creacion_boton(marco,"Nueva Suma",lambda:nuevo())
configuracion_Grid_Boton(boton2,5,1,10,10,None)
configuracion_De_Boton(boton2,"white",20,"Arial",10,"bold","italic")


etiqueta5 = creacion_Etiqueta(marco, "TOTAL")
grid_Etiqueta(etiqueta5,6,0,"w",10,10)
configurar_Etiqueta(etiqueta5,"white",20,"Arial",10,"bold","w")
texto2 = creacion_Texto (marco,total)
grid_Texto(texto2,6,1,"w",10,10)

boton3 = creacion_boton(marco,"SALIR",lambda:salir())
configuracion_Grid_Boton(boton3,7,0,10,10,2)
configuracion_De_Boton(boton3,"gray",40,"Arial",12,"bold","italic")

etiqueta6 = creacion_Etiqueta(marco,"** SERVICIOS ESPECIALES **")
grid_Etiqueta(etiqueta6,1,2,"w",10,10)
configurar_Etiqueta(etiqueta6,"lightgray",None,"Rockwell",12,"bold","w")

flete = IntVar()
garantia = IntVar()


chkflete = Checkbutton(marco,text="Flete", variable= flete, onvalue= 1, offvalue=0)
chkflete.grid(row=2,column=2,sticky="w",padx=10,pady=10)
chkflete.config(fg="black",bg="white",width=15,font=("Rockwell",10),anchor="w")

chkgar = Checkbutton(marco,text="Garantia Ectendida", variable= garantia,onvalue=1,offvalue=0)
chkgar.grid(row=3,column=2,sticky="w",padx=10,pady=10)
chkgar.config(fg="black",bg="white",width=15,font=("Rockwell",10),anchor="w")


cli = IntVar(value=1)
eot=IntVar()

cate=Radiobutton(marco,text="Cliente",variable=cli,value=1)
cate.grid(row=2,column=3,sticky="w",padx=10,pady=10)
cate.config(fg="black",bg="white",width=15,font=("Rockwell",10),anchor="w")

cate2 = Radiobutton(marco,text="No clientes",variable=cli,value=2)
cate2.grid(row=3,column=3,sticky="w",padx=10,pady=10)
cate2.config(fg="black",bg="white",width=15,font=("Rockwell",10),anchor="w")

raiz.mainloop()