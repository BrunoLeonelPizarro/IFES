from tkinter import *

raiz = Tk()
raiz.resizable(True,True)
raiz.title("**CALCULO DE COMPRAS**")
raiz.config(cursor="star")
raiz.iconbitmap('IFES/Interfaz Grafica/Iconos/compu.ico')

marco = Frame(raiz, bg= "blue", width= 600, height= 500)
marco.pack(fill="none",expand="true")
marco.config(bg = "gray", width=600, height=500)

etiqueta1 = Label(marco, text = "Sumatoria de N°")
etiqueta1.grid(row=0,column=0,sticky="w",padx=10,pady=10)
etiqueta1.config(fg="green", bg = "lightgray",width=35, font= ("Fontel",12))

etiqueta2 = Label(marco, text = "Ingrese el valor  N°1")
etiqueta2.grid(row=1,column=0,sticky="w",padx=10,pady=10)
etiqueta2.config(fg="green", bg = "lightgray",width=35, font= ("Fontel",12))

etiqueta3 = Label(marco, text = "Ingrese el valor  N°2")
etiqueta3.grid(row=2,column=0,sticky="w",padx=10,pady=10)
etiqueta3.config(fg="green", bg = "lightgray",width=35, font= ("Fontel",12))

etiqueta4 = Label(marco, text = "Ingrese el valor  N°3")
etiqueta4.grid(row=3,column=0,sticky="w",padx=10,pady=10)
etiqueta4.config(fg="green", bg = "lightgray",width=35, font= ("Fontel",12))

raiz.mainloop()