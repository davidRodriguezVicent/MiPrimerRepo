productos = [
    {
        'id':1,
        'titulo': 'Leche desnatada',
        'precio': 0.65,
        'cantidad': 3
    },
    {
        'id':2,
        'titulo': 'Carne',
        'precio': 4.25,
        'cantidad': 1
    },
    {
        'id':3,
        'titulo': 'Pan',
        'precio': 0.30,
        'cantidad': 6
    },
    {
        'id':4,
        'titulo': 'Huevos',
        'precio': 1.5,
        'cantidad': 2
    },
]

cantidad = len(productos)
print(cantidad)

## puedo acceder al un unico producto completo
print(productos[1])

## puedo acceder al valor de una clave de dicho producto
print(productos[1]['titulo'])

## editar un producto
productos[1]['precio'] = 7.45

print(productos)