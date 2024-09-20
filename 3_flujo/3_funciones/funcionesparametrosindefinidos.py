def sumar(*numeros):
    # *numeros representa una tupla(lista) de parametros
    resultado = 0
    for numero in numeros:
        resultado += numero # resultado = resultado + numero
    print(resultado)

sumar(1,2)
sumar(1,2,3)
sumar(1,2,3,4,5,6,7,8,9)