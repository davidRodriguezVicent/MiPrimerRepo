nombre = "Joaquin"

# una función puede tener parametros obligatorios y optativos. Primero recibe todos los parametros obligatorios y luego los optativos.


def saludar(nombre, apellido="Perez"):
    print(f"Hola, bienvenido {nombre} {apellido}")


saludar("", 'Perez')
saludar(nombre)
