nota = float(input('Dime tu nota: '))

if nota >= 0 and nota < 5:
    print('suspenso')

if nota >= 5 and nota <= 10:
    print('aprobado')

print('-' * 60)

# else es una secuencia de escape deberia solo usarse para valores no esperados.
if nota >= 5 and nota <= 10:
    print('aprobado')
else:
    print('suspenso')
