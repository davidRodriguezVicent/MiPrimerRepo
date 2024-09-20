numero = 10

# desde 0 hasta el numero imprimir todos los numeros que hay pero sin incluir el propio numero
for i in range(numero):
    print(f"valor:{i}")

print('-' * 60)

# desde un valor inicial a uno final sin incluir este ultimo
for i in range(1, 11):
    print(f"valor:{i}")

print('-' * 60)

# desde un valor inicial a uno final pero de 2 en 2 steps
for i in range(1, 11, 2):
    print(f'valor:{i}')

print('-' * 60)
# tambien me permite trabajar de forma invertida
for i in range(10, 0, -1):
    print(f'valor:{i}')
else:
    print('hace cosas si se acaba el bucle')
