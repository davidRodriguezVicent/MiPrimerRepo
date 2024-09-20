# un condicional abreviado es un condicional con secuencia de escape "USADO CORRECTAMENTE"

estado_luz = True

if estado_luz:
    print('Luz encendida')
else:
    print('Luz apagada')

# condicional abreviado
print('ENCENDIDIO') if estado_luz else print('APAGADO')

# operador ternario, una variable cambia su valor en un condicioal con secuencia de escape.
estado_factura = "pagada"
msg = ""

if estado_factura == "pagada":
    msg = "Le hemos enviado su pedido, gracias"
else:
    msg = "Debe proceder al pago del pedido"

print(msg)

mensaje = 'pedido enviado' if estado_factura == 'pagada' else 'pague por favor'
