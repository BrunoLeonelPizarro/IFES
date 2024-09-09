from tkinter import *
from tkinter import messagebox

raiz = Tk()
raiz.resizable(True, True)
raiz.title("**CALCULO DE COMPRAS**")
raiz.config(cursor="star", bg="gray")

marco = Frame(raiz, bg="lightgray", width=650, height=350)
marco.pack(fill="none", expand=True)
marco.config(bg="lightblue", width=650, height=350)

def informa():
    if minombre.get()=="":
        messagebox.showinfo("CONFIRMACION","Debes ingresar tu nombre")
    else:
        messagebox.showinfo("CONFUIRMACION",minombre.get())
        
def advertir():
    if minombre.get() == "":
        messagebox.showerror("ERROR","No ingresaste el nombre")
    else:
        messagebox.showinfo("CONFIRMACION","Nombre ingresado")

def salida():
    respuesta = messagebox.askquestion("SALIR DE APLICACION","Desea salir?")
    if respuesta == "yes":
        raiz.destroy()
    else:
        messagebox.showinfo("SALIDA","Aun sigues ahi")

cartel = Label(marco,text="**MANEJO DE VENTANAS**")
cartel.grid(row=0,column=0,sticky="w",padx=10,pady=10)

nom=Label(marco,text="Ingrese su nombre")
nom.grid(row=1,column=0,sticky="w",padx=10,pady=10)
nom.config(fg="black",bg="lightgrey", width=15,font=("Rockwell",13),anchor="w")

minombre = StringVar()

nombre1 = Entry(marco,textvariable=minombre)
nombre1.grid(row=1,column=1,sticky="w",padx=10,pady=10)
nombre1.config(fg="black",bg="lightblue",width=15,font=("Rockwell",13,"bold"))


infor=Button(marco,text="INFORMAR",command=lambda:informa())
infor.grid(row=4,column=0,padx=10,pady=10)
infor.config(fg="white",bg="blue",width=15,font=("Rockwell",14))

adver=Button(marco,text="ADVERTIR",command=lambda:advertir())
adver.grid(row=4,column=1,padx=10,pady=10)
adver.config(fg="white",bg="green",width=15,font=("Rockwell",14))

salir=Button(marco,text="SALIR",command=lambda:salida())
salir.grid(row=6,column=0,padx=10,pady=10,columnspan=2)
salir.config(fg="white",bg="blue",width=15,font=("Rockwell",14))

raiz.mainloop()