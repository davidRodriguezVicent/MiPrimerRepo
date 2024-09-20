"""
    siempre que trabajemos con un fichero lo vamos tener que abrir y cerrar cuando dejemos de usarlo. Para ello python nos provee de unas banderas que nos indican que hacemos con ese fichero.     
        Crear w(write) -> crear o sobreescribir un fichero
        Leer r(read) -> leer un fichero cualquiera.
        Actualizar a(append) -> añadir elementos a un fichero que ya existe
        
        el ciclo de manejo de un fichero es siempre el mismo y consta de tres partes:
        abrir fichero - realizar las acciones sobre el fichero W - R - A -> CERRAR EL FICHERO

"""

lista_alumnos = [
    {'nombre': 'Alex', 'nota': 9.5},
    {'nombre': 'Maria', 'nota': 7.5},
    {'nombre': 'Pepe', 'nota': 1.5},
    {'nombre': 'Laura', 'nota': 4.5},
    {'nombre': 'Raul', 'nota': 8.5},
    {'nombre': 'Juan', 'nota': 0.5},
    {'nombre': 'Marta', 'nota': 6.5},
]

# vamos a crear un fichero txt donde vamos a volcar los datos de mi lista.

def crear_fichero(nombre_fichero, datos = lista_alumnos):
    fichero = open(f"./data/{nombre_fichero}.txt", "w")
    ##fichero.write('En un lugar de la mancha\n')
    ##fichero.write('Solo se que no se nada\n')
    for student in datos:
        fichero.write(f"{student['nombre']}: {student['nota']}\n")
    
    fichero.close()
    
##crear_fichero('prueba')

crear_fichero('notas', lista_alumnos)