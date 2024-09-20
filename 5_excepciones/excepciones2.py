#finally se ejecuta siempre da igual si hay o hay acierto da igual si ejecutamos accion por el try o por except

try:
    numero1 = int(input('Dime un numero: '))
    numero2 = int(input('Dime otro numero: '))  
    print(numero1, numero2)
except ValueError:
    print("Los valores introducidos no son correctos")
finally:
    print('lo que sea')