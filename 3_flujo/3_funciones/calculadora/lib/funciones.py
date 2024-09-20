sumar = lambda n1, n2 : n1 + n2
restar = lambda n1, n2 : n1 - n2
multiplicar = lambda n1, n2 : n1 * n2

def dividir(n1,n2):
    return n1 / n2

def calcular(n1, n2, tipo = '1'):
    resultado = 0;
    tipoResultado = ""
    if tipo == '1':
        resultado = sumar(n1, n2)
        tipoResultado = 'sumar'
    elif tipo == '2':
        resultado = restar(n1, n2)
        tipoResultado = 'restar'
    elif tipo == '3':
        resultado = multiplicar(n1, n2)
        tipoResultado = 'multiplicar'
    elif tipo == '4':
        resultado = dividir(n1,n2)
        tipoResultado = 'dividir'
    else:
        tipoResultado = "-1"
        resultado = 0
    return resultado, tipoResultado