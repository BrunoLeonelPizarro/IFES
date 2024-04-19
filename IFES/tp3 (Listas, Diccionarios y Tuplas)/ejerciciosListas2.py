import os
os.system("cls")

def max_Elemento_Lista (a):
    valor_Maximo_Lista = max(a)
    return valor_Maximo_Lista

def min_Elemento_Lista (a):
    valor_Minimo_Lista = min(a)
    return valor_Minimo_Lista

def cantidad_Elementos_Lista (a):
    cantidad_Lista = len(a)
    return cantidad_Lista


lista1 = [1,3,5,7,9]
lista2 = [2,4,6,8,10]

print("Lista impar:", lista1);input()
print("Lista par:",lista2);input()

lista3 = lista1 + lista2

print("El elemento maximo de la lista 1 es", max_Elemento_Lista(lista1))
print("el elemento maximo de la lista 2 es", max_Elemento_Lista(lista2));input()
print("El elemento minimo de la lista 1 es", min_Elemento_Lista(lista1))
print("El elemento minimo de la lista 2 es", min_Elemento_Lista(lista2));input()
print("La cantidad de elementos de la lista 1 es de", cantidad_Elementos_Lista(lista1))
print("La cantidad de elementos de la lista 2 es de:", cantidad_Elementos_Lista(lista2));input()
print("La lista 1 concatenada con la lista 2 da como resultado:", lista3)
