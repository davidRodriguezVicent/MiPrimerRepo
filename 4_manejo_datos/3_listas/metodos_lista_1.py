lista_nombres = ['Miguel','Carlos', 'Nerea','Marcos', 'Rodrigo', 'Miguel']

#agregar un unico elemento a la lista
lista_nombres.append('Juan')
print('append', lista_nombres)

# agregar varios elementos dentro de la lista por el final
lista_nombres.extend(['Pepe', 'Lucia', 'Marta'])
print('extend', lista_nombres)

# agredar elementos de uno en uno en cualquier posicion de la lista.
lista_nombres.insert(1, 'Daniel')
print('insert', lista_nombres)

#borrar puedo borrar por posicion y por dato

#borrar el ultimo elemento de la lista.
ultimo_elemento = lista_nombres.pop()
print(ultimo_elemento)
print(lista_nombres)

# borrar por posicion en la lista. Una lista que empieza en posicion 0 y acaba en n-1 siendo la len() longitud de la lista.
elemento_cuatro = lista_nombres.pop(4) ## soporta numeros negativos empezando por el final.
print(elemento_cuatro)
print(lista_nombres)

# borrar por contenido, solo borra el primer elemento que se encuentr con ese contenido.
lista_nombres.remove('MIGUEL'.title())
print(lista_nombres)

#vaciar una lista
lista_nombres.clear()
print(lista_nombres)

#borrar una lista
del lista_nombres
