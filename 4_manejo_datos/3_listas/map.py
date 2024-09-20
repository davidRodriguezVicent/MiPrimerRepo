# mapear una lista, es aplicar sobre cada elemento de la propia lista la misma operacion
lista_numeros = [1,2,3,4,5,6,7]
lista_numeros_dobles = list(map( lambda numero: numero * 2, lista_numeros ))
print(lista_numeros_dobles)


lista_bucle = []
for numero in lista_numeros:
    lista_bucle.append(numero * 2)
    
print(lista_bucle)


lista_nombres = ['Miguel','Carlos', 'Nerea','Marcos', 'Rodrigo', 'Miguel']
lista_nombres_minuscula = list(map(lambda nombre: nombre.upper(), lista_nombres))

print(lista_nombres_minuscula)


# aplicaremos un map() a una lista de diccionarios
lista_usuarios = [
    {'name': 'Juan', 'surname': 'Perez'},
    {'name': 'Pepe', 'surname': 'Lopez'},
    {'name': 'Maria', 'surname': 'Gutierrez'},
    {'name': 'Teresa', 'surname': 'Alcalde'},
    {'name': 'Raul', 'surname': 'Rodriguez'},
    {'name': 'Lucia', 'surname': 'Torres'},
    {'name': 'Marta', 'surname': 'Serrano'},
]

lista_nombres_completos = list(map( lambda usuario: f"{usuario['name']} {usuario['surname']}", lista_usuarios))
print(lista_nombres_completos)