# Una tupla es una lista de elementos inmutable, no se puede ni añadir ni modificar elementos.
tupla = ('Juan', 42, True)
frutas = ('naranja', 'manzana', 'cereza', 'platano')
conexion = ('192.168.1.10', 'admin', 'Asdfds235464', True)

print(frutas)
print(tupla)

#longitud
print( len(frutas) )  #4

# una tupla se numera de 0 a n-1 siendo n la longitud de la tupla
#imprimir a sacar a una variable los elementos de una tupla
print(frutas[1]) # manzana
print(frutas[-2]) # cereza

# ERROR la tupla es inmutable no se puede cambiar 
# frutas[0] = "mandarina" no puedo modificar 
# frutas[5] = "melocoton" no puedo añadir elementos nuevos

# copiar tupla
frutas2 = frutas[0:3] #'naranja', 'manzana', 'cereza',
print(frutas2)
frutas3  = frutas[0:3:2] #'naranja', 'cereza',
print(frutas3)

print("-"*30)

for i in range(0, len(frutas)):
    print(frutas[i])
    

print("-"*30)

for fruta in frutas:
    print(fruta)
    

#eliminar la tupla
del frutas3
print(frutas3)