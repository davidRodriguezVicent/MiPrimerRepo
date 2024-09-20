# Escribir un programa que me permita ordenar una lista de tuplas en orden ascendente, basandome en el segundo elemento tupla

lista_frutas = [ ('Manzana', 15), ('Platano', 8), ('Fresa',12), ('Melocoton',2)]

def ordenar_lista(lista):
    lista.sort(key= lambda item: item[1], reverse= True)
    print(lista)


ordenar_lista(lista_frutas)