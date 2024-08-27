from tkinter import *

raiz = Tk()
raiz.title("Ejemplo de colores")
#--------que la ventana se maximice--------------#
raiz.resizable(True,True)
#------------------------------------------------#

#----------Configurar aspecto de la ventana raiz----------#
#bg: Color
#width: Ancho
#height: largo
raiz.config(bg="grey", width="800",height="450")
#---------------------------------------------------------#

raiz.mainloop()