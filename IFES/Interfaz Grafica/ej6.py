from tkinter import *

raiz = Tk()
raiz.title("primera ventana con etiqueta y cuadro de texto")
raiz.resizable (True,True)
raiz.config(bg= "green")





marco = Frame(raiz, bg="lightgray",width="650",height="350")
marco.pack(fill= "none", expand= "true")
marco.config(bg="lightgray", width="650",height="350")

etiqueta1 = Label(marco, text="Ingrese el primer valor")
etiqueta1.grid(row= 0,column=0)
texto1=Entry(marco)
texto1.grid(row=0, column= 1)

raiz.mainloop()
