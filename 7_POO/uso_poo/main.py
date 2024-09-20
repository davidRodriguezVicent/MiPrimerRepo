from calculadora import Calculadora

def main():
    menu = """¿Que operación quieres realizar?
    [1] sumar
    [2] restar
    [3] multiplicar
    [4] salir
    """
    opcion = input(menu)
    resultado = 0;
    casio = Calculadora()
    
    if opcion == '1':
        numero1 = int(input('Dime un numero: '))
        numero2 = int(input('Dime otro numero: '))
        resultado = casio.sumar(numero1, numero2)
        print(f'La suma de {numero1} y {numero2} es igual a {resultado}')
        pass
    elif opcion == '2':
        #restando
        numero1 = int(input('Dime un numero: '))
        numero2 = int(input('Dime otro numero: '))
        resultado = casio.restar(numero1, numero2)
        print(f'La resta de {numero1} y {numero2} es igual a {resultado}')
        pass
    elif opcion == '3':
        #multiplicando
        numero1 = int(input('Dime un numero: '))
        numero2 = int(input('Dime otro numero: '))
        resultado = casio.multiplicar(numero1, numero2)
        print(f'La multiplicación de {numero1} y {numero2} es igual a {resultado}')
        pass
    elif opcion == '4':
        print('Hasta pronto')
    else:
        print('Elección no valida')
        main()


if __name__ == "__main__":
    main()