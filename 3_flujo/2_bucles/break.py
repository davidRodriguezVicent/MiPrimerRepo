# quiero que me des un numero por pantalla, y me muestres los primeros 3 numeros que sean divisibles por 3 entre ese numero y 100

numero = int(input('Dime un numero menor que 100: '))
contador = 3

for i in range(numero, 101):
    if i % 3 == 0:
        print(i)
        contador -= 1
    if contador == 0:
        break
else:
    print("he terminado con todos los numeros")
