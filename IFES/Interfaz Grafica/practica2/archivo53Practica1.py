from tkinter import *

raiz = Tk()
raiz.resizable(True,True)
raiz.title("**CALCULO DE COMPRAS**")
raiz.config(cursor="star", bg="pink")
raiz.iconbitmap('IFES/Interfaz Grafica/Iconos/compu.ico')

marco = Frame(raiz, bg= "blue", width= 650, height= 350)
marco.pack(fill="none",expand="true")
marco.config(bg = "gray", width=600, height=500)

etiqueta1 = Label(marco, text = "Sumatoria de N°")
etiqueta1.grid(row=0,column=0,sticky="w",padx=10,pady=10)
etiqueta1.config(fg="green", bg = "gray",width=35, font= ("Fontel",12), anchor= "w")


etiqueta2 = Label(marco, text = "Ingrese el valor  N°1")
etiqueta2.grid(row=1,column=0,sticky="w",padx=10,pady=10)
etiqueta2.config(fg="green", bg = "lightgray",width=20, font= ("Fontel",12),anchor= "w")

texto1 = Entry(marco)
texto1.grid(row = 1, column= 1, sticky="w", pady=10, padx=10)

etiqueta3 = Label(marco, text = "Ingrese el valor  N°2")
etiqueta3.grid(row=2,column=0,sticky="w",padx=10,pady=10)
etiqueta3.config(fg="green", bg = "lightgray",width=20, font= ("Fontel",12),anchor= "w")

texto2 = Entry(marco)
texto2.grid(row = 2, column= 1, sticky="w", pady=10, padx=10)

etiqueta4 = Label(marco, text = "Ingrese el valor 3° valor")
etiqueta4.grid(row=3,column=0,sticky="w",padx=10,pady=10)
etiqueta4.config(fg="green", bg = "lightgray",width=20, font= ("Fontel",12),anchor= "w")

texto3 = Entry(marco)
texto3.grid(row = 3, column= 1, sticky="w", pady=10, padx=10)

boton1 = Button(marco, text="Confirmar")
boton1.grid(row=4, column=1,pady= 10, padx= 10)
boton1.config( width=15, font=("Arial",11,"bold","italic"))

boton2 = Button(marco, text="Nueva Suma")
boton2.grid(row=4, column=0,pady= 10, padx= 10)
boton2.config(width=15, font=("Arial",11,"bold","italic"))

etiqueta5 = Label(marco, text = "TOTAL")
etiqueta5.grid(row=5,column=0,sticky="w",padx=10,pady=10)
etiqueta5.config(fg="green", bg = "lightgray",width=20, font= ("Fontel",12),anchor= "w")

texto4 = Entry(marco)
texto4.grid(row = 5, column= 1, sticky="w", pady=10, padx=10)

boton3 = Button(marco, text="Salir", command=raiz.destroy)
boton3.grid(row=6, columnspan=2,pady= 10, padx= 10)
boton3.config(width=50, font=("Arial",11,"bold","italic"))

raiz.mainloop()