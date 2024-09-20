# Operadores logicos tambien devuelven solo True o False
# and (y), or (o), not (negación)

precio = float(input('Dime un precio que buscas: '))
marca = input('De que marca quieres el dispositivo: ')
# quiero encontrar un portatil de la marca lenovo por menos de 700 euros
marca = marca.lower()  # upper()
resultado = (precio < 700) and (marca == 'lenovo')
print(resultado)


# quiero un numero que sea par o divisible por 5
mi_numero = 8
resultado = (mi_numero % 2 == 0) or (mi_numero % 5 == 0)
print(resultado)

# Negacion
is_active = False
print(not is_active)  # True
