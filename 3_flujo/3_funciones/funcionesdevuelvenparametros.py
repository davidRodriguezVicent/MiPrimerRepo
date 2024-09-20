def multiplicar(n1, n2):
    resultado = n1 * n2
    frase = "el resultado de multiplicar es: "
    return resultado, frase


mi_resultado = multiplicar(2, 2)
print(mi_resultado[1], mi_resultado[0])
