nota = float(input('dime tu nota: '))

# uso incorrecto
if nota >= 0 and nota < 5:
    print('estas suspendido')
else:
    print('estas aprobado')

# uso correcto
estado_factura = 'impagada'

if estado_factura == 'pagada':
    print('Gracias por su compra')
else:
    print('No se ha podido realizar el pago')
