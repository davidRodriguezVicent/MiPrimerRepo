lista_nombres = ['Miguel','Carlos', 'Nerea','Miguel','Marcos', 'Rodrigo', 'Miguel']

#funcion que permita mirar cuantas veces hay un elemento dentro de la lista.
cantidad = lista_nombres.count('miguel'.title())
print(cantidad)

# invertir una lista con reverse, modifica la lista original
lista_nombres.reverse()
print(lista_nombres)

# ordenar lista. Tenemos que tener en cuenta lista numericas y alfabeticas.
numeros = [12,34,5,6,74,34,6,8,1,0,9]
letras = ['a', 'F', 'D', 'i', 'b', 'A']

numeros.sort(reverse=True) # reverse me permite ordenar de mayor a menor y viceversa
print(numeros)

# alfabeto, las mayusculas van primero y luego las minusculas.
letras.sort(key=str.lower)
print(letras)

# MAX y MIN
print(max(numeros)) # 74
print(min(numeros)) # 0