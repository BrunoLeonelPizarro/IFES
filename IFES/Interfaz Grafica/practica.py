from tkinter import *


def creacion_Etiqueta (marco_Entrada, texto_A_colocar):
    etiqueta = Label(marco_Entrada, text = texto_A_colocar)
    return etiqueta

def configurar_Etiqueta(row_Entrada, column_Entrada, etiqueta_Entrada):
    etiqueta_Entrada.grid(row = row_Entrada, column= column_Entrada, sticky= "w", pady= 10, padx= 10)
    etiqueta_Entrada.config(fg= "black", bg="gray", width = 20, font = ("Arial", 12), anchor = "w")

def cracion_Texto(marco_Entrada):
    texto = Entry(marco_Entrada)
    return texto

def configurar_Texto(texto_Entrada, row_Entrada, column_Entrada):
    texto.griconfig()
raiz = Tk()
raiz.title("Practica Interfaz Grafica")
raiz.resizable(True,True)
raiz.config(bg= "gray")

marco = Frame(raiz, bg= "lightgray", width= "500", height= "500")
marco.pack(fill= "none", expand="true")
marco.config(bg = "lightgray", width= 500, height= 800)

etiqueta1 = creacion_Etiqueta(marco, "Ingrese el Nombre")
configurar_Etiqueta(0,0,etiqueta1)
etiqueta2 = creacion_Etiqueta(marco, "Ingrese el Apellido")
configurar_Etiqueta(1,0,etiqueta2)
etiqueta3 = creacion_Etiqueta(marco, "Ingrese la edad")
configurar_Etiqueta(3,0,etiqueta3)
etiqueta4 = creacion_Etiqueta(marco, "Ingrese el DNI")
configurar_Etiqueta(4,0,etiqueta4)
etiqueta5 = creacion_Etiqueta(marco, "Ingrese la ciudad")
configurar_Etiqueta(5,0,etiqueta5)



raiz.mainloop()
