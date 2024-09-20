frase = "El coche de Joaquin es un Ferrari rojo"
# Joaquin -> David
frase = frase.replace('Joaquin', 'David')
print(frase)

otra_frase = 'Ho)laÇmundoÇdes)deÇpython'
otra_frase = otra_frase.replace('Ç', ' ').replace(')', '')
print(otra_frase)

# eliminar el espacio en blanco por delante y por detras de una palabra
nombre = "      Juan Antonio      "
# elimina caracteres en blanco por ambos lados
print('hola ' + nombre.strip() + ", bienvenido")
print('hola ' + nombre.rstrip() + ", bienvenido")
print('hola ' + nombre.lstrip() + ", bienvenido")

frase2 = "Hola Mundo"
palabraFinal = frase2[5:]
print(palabraFinal)
