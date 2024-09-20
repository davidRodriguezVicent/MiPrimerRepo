nota = input('Dime la nota: ')
nota = float(nota[0:5])


# Recordar que la programacion es es mejor buscar al opcion más restrictiva y empezar por ahi. Casi siempre suelen operaciones negativas o contrarias.

if nota >= 0 and nota < 5:
    print('SUSPENSO')
elif nota >= 5 and nota <= 10:
    print('APROBADO')
else:
    print('Nota no es valida')


if nota >= 0 and nota < 5:
    print('suspenso')
elif nota >= 5 and nota < 6:
    print('suficiente')
elif nota >= 6 and nota < 7:
    print('bien')
elif nota >= 7 and nota < 9:
    print('notable')
elif nota >= 9 and nota <= 10:
    print('sobresaliente')
else:
    print('nota no valida')
