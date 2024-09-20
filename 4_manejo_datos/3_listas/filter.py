lista_numeros = [3,1,2,3,4,5,6,7,3,454,67,7,3245,8778,56,34,55]

lista_bucle = []
for numero in lista_numeros:
    if numero % 2 != 0:
        lista_bucle.append(numero)
        
print(lista_bucle)

#filtrar de esta lista solo los numeros impares.

lista_impares = list(filter(lambda numero: numero % 2 != 0, lista_numeros))
print(lista_impares)

# vamos aplicar ester filter sobre una lista de diccionarios. 
alumnos = [
    { 'nombre': 'Juan', 'edad':12 },
    { 'nombre': 'Maria', 'edad':10 },
    { 'nombre': 'Rocio', 'edad':18 },
    { 'nombre': 'Manuel', 'edad':19 },
    { 'nombre': 'Israel', 'edad':11 },
    { 'nombre': 'Teresa', 'edad':7 },
    { 'nombre': 'Pablo', 'edad':21 },
]

# aquellos alumnos que son menores de edad
def filterByAge(age_min, student_list):
    filter_list = list( filter(lambda alumno: alumno['edad'] < age_min, student_list) )
    return filter_list

lista_menores_18 = filterByAge(18, alumnos)
lista_menores_10 = filterByAge(10, alumnos)
print(lista_menores_18)
print(lista_menores_10)