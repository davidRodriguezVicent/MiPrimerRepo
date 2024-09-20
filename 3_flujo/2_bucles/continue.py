# pido un numero y quiero todos los numeros impares desde el 0 hasta ese numero

numero = 28

for i in range(numero):
    if i % 2 != 0:
        print(i)

print('---------------------')

for i in range(numero):
    if i % 2 == 0:
        continue
    print(i)
else:
    print('he llegado a final del bucle')
