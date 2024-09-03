from tkinter import *

raiz = Tk()
raiz.title("tercera ventana con etiqueta y cuadro de texto")
raiz.resizable (True,True)
raiz.config(bg= "pink")

marco = Frame(raiz, bg="lightgray",width="650",height="350")
marco.pack(fill= "none", expand= "true")
marco.config(bg="sky blue", width="650",height="350")

etiqueta1 = Label(marco, text="Ingrese el 1° valor:")
etiqueta1.grid(row= 0,column=0, sticky= "w", pady=10,padx=10)
etiqueta1.config(fg= "blue", bg = "white", width = 35, font = ("Arial",12))

texto1=Entry(marco)
texto1.grid(row=0, column= 1,sticky= "w", pady=10,padx=10)

etiqueta2 = Label(marco, text="Ingrese el 2° valor:")
etiqueta2.grid(row= 1,column=0, sticky= "w", pady=10,padx=10)
etiqueta2.config(fg= "blue", bg = "white", width = 35, font = ("Arial",12))

texto2=Entry(marco)
texto2.grid(row=1, column= 1, sticky= "w", pady=10,padx=10)

etiqueta3 = Label(marco, text="Ingrese el 3° valor:")
etiqueta3.grid(row= 2,column=0, sticky= "w", pady=10,padx=10)
etiqueta3.config(fg= "blue", bg = "white", width = 35, font = ("Arial",12))

texto3=Entry(marco)
texto3.grid(row=2, column= 1, sticky= "w", pady=10,padx=10)

raiz.mainloop()