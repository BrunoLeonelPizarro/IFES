from tkinter import *

raiz = Tk()
raiz.title("Ventana nueva reliece - Corazon")
raiz.resizable(True, True)
raiz.config(cursor="heart")
raiz.config(relief="sunken")
raiz.config(bd=30)

marco = Frame()
marco.pack()
marco.config(bg = "pink", width= "650", height="350")
marco.pack(fill = "both", expand=1)


raiz.mainloop()