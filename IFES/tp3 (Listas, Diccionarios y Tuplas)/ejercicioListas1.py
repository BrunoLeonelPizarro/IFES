lista1 = ["Luis","Veronica","Sergio","Leandro","Franco"]
lista2 = ["Pereira","Martinez","Silva","Fernandez","Sepulveda"]
lista3 = ["21","45","28","22","25"]

def reversoLista (a):
    revLista = a.reverse()
    return revLista

print(reversoLista(lista2))

lista1.append("Bruno")
lista1.append("Nehuen")
lista1.append("Santino")
print("Se agregaron 3 elementos a la lista de nombres")
print(lista1);input()

lista2.append("Pizarro")
lista2.append("Gutierrez")
lista2.append("Andes")
print("Se agregaron 3 nuevos elementos a la lista de apellidos")
print(lista2);input()

lista3.append("21")
lista3.append("22")
lista3.append("23")
print("Se agregaron 3 nuevos elementos a la lista de edades")
print(lista3);input();