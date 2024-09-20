# try - excerpt
## try gestiona la parte correcta - except gestiona lo que se haría si salta un error.
# https://docs.python.org/3/library/exceptions.html

def main():
    try:
        numero1 = int(input('Dime un numero: '))
        numero2 = int(input('Dime otro numero: '))
        print(numero1, numero2)
    except ValueError:
        print('Los valores introducidos no son correctos, vuelve a intentarlo')
        main()


#main()

def dividir(n1,n2):
    try:
        resultado = n1 / n2
        print(resultado)
    except ZeroDivisionError:
        print('No es posible dividir por cero')
    except: # gestion de error generico
        print('Ha ocurrido un error y el resultado no es el esperado')

dividir(12,'hola')