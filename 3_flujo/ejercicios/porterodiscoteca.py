# Pedimos la edad por pantalla y si es menor que 18 no le dejamos pasar y si es mayor le dejamos pasar.
# Ojo cuidado con las condiciones observar el mejor sistema condicional
edad = int(input('Dime tu edad: '))
EDAD_CORTE = 18

if edad >= EDAD_CORTE:
    print('Bienvenido')
else:
    print('No puedes pasar')


if edad >= 0 and edad < EDAD_CORTE:
    print('Un vasito de leche y la cama')
elif edad >= EDAD_CORTE and edad <= 100:
    print('Bienvenido!!')
else:
    print('Edad no valida')
