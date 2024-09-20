texto = "Maria12"
print(texto.isdigit())  # True
print(texto.isalpha())  # False
print(texto.isalnum())  # True

print('-' * 60)

# una cadena de caracter empieza o termina en algo concreto
texto2 = "En un lugar de la Mancha"
print(texto2.lower().endswith('mancha'))  # True
print(texto2.lower().startswith('En'))  # False

print('-' * 60)

cadena = "juan antonio"
print(cadena.isupper())  # valida que toda la cadena es totalmente en mayusculas
print(cadena.islower())  # valida que toda la cadena es totalmente en minusculas
print(cadena.istitle())  # valida que toda la cadena es totalmente en titulo
