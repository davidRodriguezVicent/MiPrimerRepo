nombre = "Juan"
apellido = "Perez"
edad = 42
separador = " - "

texto = f"{nombre}{separador}{apellido}{separador}{edad}"
print(texto)

otro_texto = separador.join([nombre, apellido, str(edad)])
print(otro_texto)


# partir cadenas de caracter
frase = "Hola mundo desde python"
cadenas = frase.partition(' ')
print(cadenas)

# dividir en varios bloque split
palabras = frase.split(" ")
print(palabras)


cadena = """Hola Mundo
desde el maravilloso
lenguaje de python"""

filas = cadena.splitlines()
print(filas)
print(filas[0].split(" "))
