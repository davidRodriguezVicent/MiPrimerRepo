# calcular el area de un poligono (alto * ancho)

alto = input('Dime la altura de mi poligono: ')
ancho = float(input('Dime la anchura del poligono: '))
alto = float(alto)  # int(alto)
area = alto * ancho

print('El area de tu poligono es: ' + str(area))

# Templates string - templates de texto - fprint
print(f'El area del poligono que tiene un {
      ancho} de ancho y {alto} de alto es {area}')
