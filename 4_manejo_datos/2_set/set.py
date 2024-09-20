# Conjunto de elementos desordenados UNICOS y no repetidos
frutas = {'naranja', 'manzana', 'cereza', 'manzana', 'platano', 'manzana'}
print(frutas)

lista = [1,1,1,1,3,2,4,5,6,4,5,8,97,7,9,8,5,6]
print(lista)
conjunto = set(lista)
print(conjunto)
lista_no_duplicados = list(conjunto)
print(lista_no_duplicados)
# un set es un conjunto de datos ordenados de forma aleatoria, no tiene posicion

# ERROR, set no tiene posicion por que es aleatorio
# print(frutas[0])

#agrear elemento
frutas.add('melon')
print(frutas)

#borrar elementos de un set que sepamos seguro que existen dentro del set
frutas.remove('melon')
print(frutas)

#borrar elementos sin saber si existen o no en el set.
frutas.discard('sandia')
print(frutas)

#vaciar el set
frutas.clear()
print(frutas)
#borrar el set
del(frutas)