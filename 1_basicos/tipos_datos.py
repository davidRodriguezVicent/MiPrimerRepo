# Tipos de datos en python

# Cadena de caracteres o char - string
nombre = "Juan"
apellidos = 'Perez'

texto = '''
¿ Qué opción quieres?
[1] Python
[2] Java
[3] PHP 
: '''
# print(texto)
opcion = input(texto)
print('la opcion elegida es: ' + opcion)

# numericos
edad = 23  # int
grados = -23  # negativos
precio = 9.99  # racionales o floats

# Booleanos (True y False)
estado = True
envio = False

print(type(envio))
print(type(nombre))
print(type(edad))
print(type(precio))
