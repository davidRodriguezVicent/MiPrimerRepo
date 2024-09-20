# pedir un numero por pantalla y sacar los numero divisibles por cuatro desde 0 hasta ese numero y la suma de dichos numeros.
numero = int(input('Dime un número: '))
suma = 0

for i in range(numero + 1):
    if i % 4 == 0 and i != 0:
        print(i)
        suma += i
print(f'La suma de los numeros divisibles por 4 desde 0 hasta {
      numero} son {suma}')
