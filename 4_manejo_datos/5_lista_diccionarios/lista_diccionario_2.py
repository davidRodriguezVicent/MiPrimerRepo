productos = [
    {
        'id':1,
        'titulo': 'Leche desnatada',
        'precio': 0.65,
        'cantidad': 10
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
        'cantidad': 0
    },
    {
        'id':4,
        'titulo': 'Huevos',
        'precio': 1.5,
        'cantidad': 2
    },
]

numero_productos = len(productos)

def printData(lista = productos):
    for producto in lista:
        precio = str(producto['precio'] * producto['cantidad'])[0:5]
        print('-'*60)
        print(f'{producto['id']} - {producto['titulo']}: {precio} ')
        


## crear un metodo que me permite cada vez que lo ejecute añadir elementos a la lista.
def addProduct(titulo, precio, cantidad, lista = productos):
    # cuando modifiqueis una variable global en python teneis que definirlo como global
    global numero_productos
    numero_productos += 1
    new_product = {
        'id':numero_productos,
        'titulo': titulo,
        'precio': precio,
        'cantidad': cantidad
    }
    lista.append( new_product )
  

addProduct('cereales', 3, 2)
addProduct('mejillones', 2, 10)
printData(productos)


def calcularCosteTotal(lista):
    precioTotal = 0;
    for producto in lista:
        precioTotal += producto['precio'] * producto['cantidad']
    print('Precio total: ', precioTotal)
    
calcularCosteTotal(productos)

def filterByStock(stock, lista):
    return list( filter( lambda product: product['cantidad'] <= stock, lista) ) 

productos_sin_stock = filterByStock(0, productos)
productos_con_menos_3 = filterByStock(3, productos)
print('productos sin stock', productos_sin_stock)
print('productos con menos de 3',productos_con_menos_3)