# lista o array asociativo donde se elimina el concepto de posicion y nos manejamos con concepto clave:valor

alumno = {
    'nombre': 'Juan Antonio',
    'edad': 42,
    'matricula': 'A123456',
    'estado': True
}
print(alumno)

# no tenemos indices asi que accedemos al valor de los elementos por la clave.
print(alumno['nombre']) # Juan Antonio

## getter para extraer informacion 
#como modificar un valor por su clave.
alumno['edad'] = 32
# get
print(alumno.get('edad')) # 32 si no existe no te lanza un error te devuelve none

# recorrer un diccionario, recorremos el diccionario usando claves

for key, value in alumno.items():
    print(f"{key}: {value}")
    
# solo quiero acceder al valor
for valor in alumno.values():
    print(valor)
    
# solo quiero acceder a la clave
for clave in alumno.keys():
    print(clave)
    
# añadir elementos que no existan en el diccionario
alumno['direccion'] = 'calle piso puerta numero'

print(alumno)

# borrar una clave en python
alumno.pop('direccion')

print(alumno)

# vaciar diccionario 
alumno.clear()

# borrar el diccionario
del alumno
    
