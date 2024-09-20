#Lista es un conjutno de elementos desordenado, tiene longitud, tiene posicion, no es immutable. Es decir podemos aumentar o disminuir la lista, y cambiar elementos de la misma en una posicion concreta.

lista_nombres = ['Carlos', 'Nerea', 'Juan', 'Maria', 'Lucia']
lista = ['Carlos', 32, True]

#longitud
print( len(lista_nombres) ) # 5

#imprimir el valor del elemento
print(lista_nombres[2]) #Juan
print(lista[2]) # True

for nombre in lista_nombres:
    print(nombre)
else:
    print("hemos terminado la lista")
    
# son mutables cambiar elementos dentro de la lista
lista[1] = 42
print(lista)