import lib.funciones as fn

def init():
    texto = """Dime que quieres calcular
    [1] - sumar
    [2] - restar
    [3] - multiplicar
    [4] - dividir
    [x] - salir
    : """
    
    opcion = input(texto).lower();
    if opcion != 'x':
        numero1 = float(input('Dime un numero: '))
        numero2 = float(input('Dime otro numero: '))
        resultado = fn.calcular(numero1, numero2, opcion)
        print(f"El resultado de {resultado[1]} {numero1} y {numero2} es {resultado[0]}") if resultado[1] != '-1' else print('Operacion no valida')
    else:
        print('Muchas gracias, hasta la proxima')
    


if __name__ == "__main__":
    init()