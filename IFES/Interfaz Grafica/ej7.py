from tkinter import *

raiz = Tk()
raiz.title("segunda ventana con etiqueta y cuadro de texto")
raiz.resizable (True,True)
raiz.config(bg= "green")

marco = Frame(raiz, bg="lightgray",width="650",height="350")
marco.pack(fill= "none", expand= "true")
marco.config(bg="lightgray", width="650",height="350")

etiqueta1 = Label(marco, text="Ingrese el 1° valor")
etiqueta1.grid(row= 0,column=0)
texto1=Entry(marco)
texto1.grid(row=0, column= 1)

etiqueta2 = Label(marco, text="Ingrese el 2° valor")
etiqueta2.grid(row= 1,column=0)
texto2=Entry(marco)
texto2.grid(row=1, column= 1)

etiqueta3 = Label(marco, text="Ingrese el 3° valor")
etiqueta3.grid(row= 2,column=0)
texto3=Entry(marco)
texto3.grid(row=2, column= 1)

raiz.mainloop()