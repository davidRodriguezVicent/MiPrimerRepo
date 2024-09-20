import math

numero = "2"
print(type(numero))  # str

# conversion de tipos
print(int('2'))  # 2 entero
print(float('2.2'))  # 2.2 racional
print(float(3))  # 3.0 racional
print(int(2.2))  # quedarme solo con la parte entera 2. No es un redondeo.

nota = 4.999999999999999999999
print(nota)


numeroA = 3.437
redondeo = round(numeroA)
print(redondeo)

otro_numeroA = 3.14141619
print(round(otro_numeroA, 3))

print('-' * 60)
# print(round(nota, 3)) ERROR me redondearia a 5
# print(math.trunc(nota))

# para solucionar el problema de la nota tenemos jugar con las conversiones.
nota_string = input('dime nota: ')
nota = float(nota_string[0:5])
print(nota, type(nota))


# tiene libreria operaciones matematicas math
# https://docs.python.org/3/library/math.html

# redondeo a la baja
print(math.floor(numeroA))
# redondeo a la alta
print(math.ceil(numeroA))
# raiz cuadrado
print(math.sqrt(256))  # 16
# la suma una lista de numeros
print(math.fsum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
