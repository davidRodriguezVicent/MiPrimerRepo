"""
Realizar un aplicación que me permita calcular el PVP de venta de un producto para una tienda.
El programa me tiene que pedir un precio de proveedor, el impuesto que desea aplicar y el margen de beneficio que quiere tener en ese producto.
En función de estos parametros quiero calcular el precio total del producto
"""
import funciones as fn

def main():
    precio_proveedor = float(input('Dime el precio que tiene el producto: '))
    porcentaje_beneficio = float(input('Dime el porcentaje que de beneficio que deseas obtener: '))
    beneficio = porcentaje_beneficio / 100
    option = input("""Que impuesto tienes que aplicar al producto:
    [0] 21%
    [1] 10%
    [2] 4%
    Selecciona una option: """)
    tipo_impositivo = 0;
    if option == '0':
        tipo_impositivo = 0.21
    elif option == '1':
        tipo_impositivo = 0.10
    elif option == '2':
        tipo_impositivo = 0.04
    else:
        print('tipo impositivo no valido, vuelve a introducir los datos')
        main()
        
    coste_beneficio = fn.calcular_porcentaje(precio_proveedor, beneficio)
    precio_beneficio = fn.sumar(coste_beneficio, precio_proveedor)
    coste_impuesto = fn.calcular_porcentaje(precio_beneficio, tipo_impositivo)
    pvp = fn.sumar(precio_beneficio, coste_impuesto)
    print(f'El precio de venta al publico de {precio_proveedor}€ con un beneficio de {porcentaje_beneficio}% y un iva de {tipo_impositivo * 100}% es {pvp}')


if __name__ == "__main__":
    main()