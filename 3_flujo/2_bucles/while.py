# mientras que: se cumpla la condicion del bucle esta acaba

numero = 1
final = int(input('Cuantos pasos quieres que de: '))

while numero <= final:
    print(numero)
    if numero == 5:
        break
    numero += 1
else:
    print('ha terminado el bucle')


otro_numero = 10
while otro_numero > 1:
    print(otro_numero)
    otro_numero -= 2
