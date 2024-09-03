from tkinter import *

raiz = Tk()
raiz.title("tercera ventana con etiqueta y cuadro de texto")
raiz.resizable (True,True)
raiz.config(bg= "pink")

marco = Frame(raiz, bg="lightgray",width="650",height="350")
marco.pack(fill= "none", expand= "true")
marco.config(bg="sky blue", width="650",height="350")

etiqueta1 = Label(marco, text="Ingrese el 1° valor:")
etiqueta1.grid(row= 0,column=0, sticky= "w", pady=10,padx=10,)
etiqueta1.config(fg= "blue", bg = "white", width = 30, font = ("Arial",12), anchor="w")

texto1=Entry(marco)
texto1.grid(row=0, column= 1, pady=10,padx=10,sticky="w")
texto1.config(width=30)

etiqueta2 = Label(marco, text="Ingrese el 2° valor:")
etiqueta2.grid(row= 1,column=0, sticky= "w", pady=10,padx=10,)
etiqueta2.config(fg= "blue", bg = "white", width = 30, font = ("Arial",12), anchor="w")

texto2=Entry(marco)
texto2.grid(row=1, column= 1, sticky= "w", pady=10,padx=10)

etiqueta3 = Label(marco, text="Ingrese el 3° valor:")
etiqueta3.grid(row= 2,column=0, sticky= "w", pady=10,padx=10,)
etiqueta3.config(fg= "blue", bg = "white", width = 30, font = ("Arial",12), anchor="w")

texto3=Entry(marco)
texto3.grid(row=2, column= 1, sticky= "w", pady=10,padx=10)


boton1 = Button(marco, text="CONFIRMAR")
boton1.grid(row=3, column=0,pady=10,padx=10,sticky="w")
boton1.config(fg="green", bg="lightgray", width=30, font=("Arial",11,"bold","italic"))

boton2 = Button(marco, text="CANCELAR")
boton2.grid(row=3, column=1,pady=10,padx=10,sticky="w")
boton2.config(fg="red", bg="lightgray", width=30, font=("Arial",11,"bold","italic"))

raiz.mainloop()