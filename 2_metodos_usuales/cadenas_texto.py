texto = "HoLa"
otro_texto = 'en un lugar de la mancha'

"""
Python es un lenguaje multiparadigma. Existe metodos que son POO y metodos que son funcionales

    cadena.nombre_metodo() POO (programacion orientada a objeto)
    nombre_function(valor) Metodología funcional -> devuelve un valor con la transformacion
    
"""
# estos metodos no modifican la variables original, salvo que la sobrescribamos.

print(otro_texto.capitalize())  # En un lugar de la mancha
print(otro_texto.lower())  # en un lugar de la mancha
print(otro_texto.upper())  # EN UN LUGAR DE LA MANCHA
print(texto.swapcase())  # hOlA
print(otro_texto.title())  # En Un Lugar De La Mancha
print(otro_texto)
print(texto)

texto_mayuscula = texto.upper()

# a veces necesitamos que varias cadenas tenga la mis longitud

dni = "456789Y"
print(dni.zfill(9))

# metodos de busqueda dentro de un string o cadena
frase = "SOlo se que no se nada"

# cuantas Ós hay en la cadena de caracter
print('numero de oes', frase.lower().count('o'))

# puedo saber la longitud de una cadena caracter
print(len(frase))


# extraer una cantidad concreta de caracteres de una frase
palabra = frase[0:4]  # SOlo
print(palabra)
otra_palabra = frase[8:11]  # que
print(otra_palabra)
