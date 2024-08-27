from tkinter import *

raiz = Tk()
raiz.title("Creando frame")
raiz.resizable(True, True)
raiz.config(bg = "grey")

#---------Crea otra ventana dentro de la raiz------------#
marco = Frame()
#--------------------------------------------------------#

#----------------Le indica al frame que va dentro de la ventana raiz----------------#
marco.pack()
#-----------------------------------------------------------------------------------#

#------------Configura las medidas del frame----------#
marco.config(bg="white", width="800",height="350")
#-----------------------------------------------------#

raiz.mainloop()

