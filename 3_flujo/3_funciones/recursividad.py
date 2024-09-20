#Recursividad son funciones que se llaman a si mismas. Hacer un bucle sin tener un bucle

# Crear un funcion que pida por parametro saber si una cadena de caracters es numerica.


def is_string_number():
    numero = input('Dime un numero: ')
    if numero.isdigit():
        print('Gracias por darme un numero')
    else:
        print('Esto es alfanumerico, vuelve a introducir el numero: ')
        is_string_number()
        
is_string_number()