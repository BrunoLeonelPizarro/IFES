from tkinter import *
import sqlite3

def creacion_Label(Entrada_Marco, texto_A_Colocar):
    etiqueta = Label(Entrada_Marco,text= texto_A_Colocar)
    return(etiqueta)

def grid_Label(entrada_Label,Entrada_Row,entrada_Column,entrada_stincky,entrada_Pady,entrada_padx):
    entrada_Label.grid(row=Entrada_Row,column= entrada_Column,stincky= entrada_stincky , pady=entrada_Pady,padx= entrada_padx)

def configuracion_Label (Entrada_Label,Entrada_bg,Entrada_width, Entrada_Fuente, Entrada_tamanio_Fuente, Entrada_bold, Entrada_italic, Entrada_Anchor):
    Entrada_Label.config(bg= Entrada_bg,width = Entrada_width, font = (Entrada_Fuente, Entrada_tamanio_Fuente, Entrada_bold, Entrada_italic), anchor = Entrada_Anchor)

def creacion_Entry(Entrada_Marco):
    entry = Entry(Entrada_Marco)
    return entry

def configuracion_Entry (Entrada_Entry,Entrada_bg,Entrada_width, Entrada_Fuente, Entrada_tamanio_Fuente, Entrada_bold, Entrada_italic, Entrada_Anchor):
    Entrada_Entry.config(bg= Entrada_bg,width = Entrada_width, font = (Entrada_Fuente, Entrada_tamanio_Fuente, Entrada_bold, Entrada_italic), anchor = Entrada_Anchor)

def creacion_Button(Entrada_Marco,Texto_A_Colocar, comando_A_Asignar):
    button = Button(Entrada_Marco,text=Texto_A_Colocar, command= lambda:comando_A_Asignar)
    return button

def grid_Label(entrada_Label,Entrada_Row,entrada_Column,entrada_stincky,entrada_Pady,entrada_padx):
    entrada_Label.grid(row=Entrada_Row,column= entrada_Column,stincky= entrada_stincky , pady=entrada_Pady,padx= entrada_padx)

def configuracion_ (Entrada_Button,Entrada_bg,Entrada_width,Entrada_columnSpan, Entrada_Fuente, Entrada_tamanio_Fuente, Entrada_bold, Entrada_italic, Entrada_Anchor):
    Entrada_Button.config(bg= Entrada_bg,width = Entrada_width,columnspan = Entrada_columnSpan, font = (Entrada_Fuente, Entrada_tamanio_Fuente, Entrada_bold, Entrada_italic), anchor = Entrada_Anchor)


def creacion_Checkb(Entrada_Marco,texto_A_Colocar, variable_A_Asignar):
    checkb = Checkbutton(Entrada_Marco, text= texto_A_Colocar, onvalue=1, offvalue=0, variable= variable_A_Asignar)
    return checkb

def grid_Label(entrada_Label,Entrada_Row,entrada_Column,entrada_stincky,entrada_Pady,entrada_padx):
    entrada_Label.grid(row=Entrada_Row,column= entrada_Column,stincky= entrada_stincky , pady=entrada_Pady,padx= entrada_padx)

def configuracion_CheckB (Entrada_checkB,Entrada_bg,Entrada_width, Entrada_Fuente, Entrada_tamanio_Fuente, Entrada_bold, Entrada_italic, Entrada_Anchor):
    Entrada_checkB.config(bg= Entrada_bg,width = Entrada_width, font = (Entrada_Fuente, Entrada_tamanio_Fuente, Entrada_bold, Entrada_italic), anchor = Entrada_Anchor)

def creacion_RadioB (Entrada_Marco, texto_A_Colocar, valor_Radio,variable_A_Colocar):
    radio_Button = Radiobutton(Entrada_Marco, text= texto_A_Colocar, value=valor_Radio, variable= variable_A_Colocar)
    return radio_Button

def grid_Label(entrada_Label,Entrada_Row,entrada_Column,entrada_stincky,entrada_Pady,entrada_padx):
    entrada_Label.grid(row=Entrada_Row,column= entrada_Column,stincky= entrada_stincky , pady=entrada_Pady,padx= entrada_padx)

def configuracion_RadioB (Entrada_RadioB,Entrada_bg,Entrada_width, Entrada_Fuente, Entrada_tamanio_Fuente, Entrada_bold, Entrada_italic, Entrada_Anchor):
    Entrada_RadioB.config(bg= Entrada_bg,width = Entrada_width, font = (Entrada_Fuente, Entrada_tamanio_Fuente, Entrada_bold, Entrada_italic), anchor = Entrada_Anchor)




raiz = Tk()
raiz.resizable(True,True)

raiz.iconbitmap('IFES/Interfaz Grafica/Iconos/compu.ico')
raiz.title("Confiteria lo de tito calderon")
raiz.config(bg="lightblue")

precio_Emp_Carne = IntVar()
precio_Emp_Pollo = IntVar()
precio_Pizza = IntVar()
precio_Lomo = IntVar()

marco = Frame(raiz)
marco.pack(fill=None,expand=True)
marco.config(bg="pink", width= 620, height = 600)

texto1 = Label(marco,text="Bienvenido!")
texto1.grid(row=0,column=0, columnspan=2,padx=10,pady=10)
texto1.config(bg="pink",fg="red",font=("Rockwell",10,"bold"))

texto2 = texto1 = Label(marco,text="¿Que comidas eligio el cliente?")
texto2.grid(row=2,column=0,sticky="w",padx=10,pady=10)
texto2.config(bg="pink",width=30,fg="black",font=("Rockwell",10,"bold"),anchor="w")

texto2 = texto1 = Label(marco,text="Cantidades")
texto2.grid(row=2,column=1,padx=10,pady=10)
texto2.config(bg="pink",width=10,fg="black",font=("Rockwell",10,"bold"),anchor="w")


chkEmp_Pollo = Checkbutton(marco,text="Empanada de pollo",variable=precio_Emp_Pollo, onvalue= 1, offvalue=0)
chkEmp_Pollo.grid(row=3,column=0,sticky="w",padx=10,pady=10)
chkEmp_Pollo.config(fg="black",bg="pink",width=16,font=("Rockwell",10),anchor="w")


texto_Cantidad = Entry(marco)
texto_Cantidad.grid(row=3,column=1,sticky="w",padx=10,pady=10)
texto_Cantidad.config(bg="white",width=4)

chkEmp_Carne = Checkbutton(marco,text="Empanada de Carne",variable=precio_Emp_Carne, onvalue= 1, offvalue=0)
chkEmp_Carne.grid(row=4,column=0,sticky="w",padx=10,pady=10)
chkEmp_Carne.config(fg="black",bg="pink",width=17,font=("Rockwell",10),anchor="w")


texto_Cantidad = Entry(marco)
texto_Cantidad.grid(row=4,column=1,sticky="w",padx=10,pady=10)
texto_Cantidad.config(bg="white",width=4)

chk_Pizza = Checkbutton(marco,text="Pizza",variable=precio_Pizza, onvalue= 1, offvalue=0)
chk_Pizza.grid(row=6,column=0,sticky="w",padx=10,pady=10)
chk_Pizza.config(fg="black",bg="pink",width=16,font=("Rockwell",10),anchor="w")

texto_Cantidad = Entry(marco)
texto_Cantidad.grid(row=6,column=1,sticky="w",padx=10,pady=10)
texto_Cantidad.config(bg="white",width=4)

chk_Lomo = Checkbutton(marco,text="Lomo",variable=precio_Lomo, onvalue= 1, offvalue=0)
chk_Lomo.grid(row=7,column=0,sticky="w",padx=10,pady=10)
chk_Lomo.config(fg="black",bg="pink",width=16,font=("Rockwell",10),anchor="w")

texto_Cantidad = Entry(marco)
texto_Cantidad.grid(row=7,column=1,sticky="w",padx=10,pady=10)
texto_Cantidad.config(bg="white",width=4)

texto3 = Label(marco,text="Tipo de retiro")
texto3.grid(row=2,column=2,padx=10,pady=10)
texto3.config(bg="pink",width=11,fg="black",font=("Rockwell",10,"bold"),anchor="w")


Rbutton_Delivery = Radiobutton(marco,text="Con Delivery",value=1,variable=None)
Rbutton_Delivery.grid(row=3, column=2,padx=10,pady=10,sticky="w")
Rbutton_Delivery.config(bg="pink")
Rbutton_Local = Radiobutton(marco,text="Retiro en el local",value=2,variable=None)
Rbutton_Local.grid(row=4, column=2,padx=10,pady=10,sticky="w")
Rbutton_Local.config(bg="pink")

boton_Calcular= Button(marco,text="CALCULAR",command=None)
boton_Calcular.grid(row=5,column=2,padx=10,pady=10)
boton_Calcular.config(bg="lightgray",fg="green",width=10,font=("Arial",12,"bold"))







raiz.mainloop()