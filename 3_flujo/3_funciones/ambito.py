# Ambito funcional y ambito bloque
# Python no tiene ambito de bloque
# FUNCIONAL: una variable creada fuera de una función es global y se puede usar dentro de funcion de script. Si declaro una variable dentro de una funcion esta el local y solo se puede usar dentro de esa función.
# BLOQUE: (python no lo tiene). Las variables creadas dentro de cualquier estructura de flujo (condicionales, bucles, funciones) son de ambito local.

frase = "El resultado es: "  # GLOBAL


def potencia(base, exponente):
    resultado = base ** exponente  # ambito local
    frase = "pepe"
    print(frase, resultado)


potencia(2, 2)
print(frase)

# Esto no es muy recomendable. Si por alguna puntual necesito modificar el valor de una variable global dentro de una funcion
# Tenemos que usar el prefijo global

suma = 0


def sumar(n1, n2):
    global suma
    suma = n1 + n2
    # print(suma)


sumar(2, 4)
print(suma)
