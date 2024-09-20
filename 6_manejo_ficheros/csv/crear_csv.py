import csv

lista_empleados = [
    {'id': 1, 'nombre': 'Juan Antonio', 'apellidos': 'Pérez Jarillo', 'correo': 'jj@gmail.com', 'departamento': 'Desarrollo' },
    {'id': 2, 'nombre': 'Almudena', 'apellidos': 'González Camuñas', 'correo': 'almu@gmail.com', 'departamento': 'Finanzas' },
    {'id': 3, 'nombre': 'Marta', 'apellidos': 'Rodriguez Lopez', 'correo': 'marta@gmail.com', 'departamento': 'Marketing' },
    {'id': 4, 'nombre': 'Joaquin', 'apellidos': 'Calvo Lopez', 'correo': 'joaquin@gmail.com', 'departamento': 'Finanzas' },
    {'id': 5, 'nombre': 'Lucia', 'apellidos': 'Pérez Alvárez', 'correo': 'lucia@gmail.com', 'departamento': 'Cuentas' },
]

def crear_csv(carpeta, fichero, lista):
    fichero = open(f'./{carpeta}/{fichero}', 'w', encoding='utf-8')
    campos = []
    for key in lista[0].keys():
        campos.append(key)
    #creo el fichero csv con solo los campos en la primera linea.
    ficherocsv = csv.DictWriter(fichero, fieldnames=campos)
    # escribir las cabeceras en esa primera linea
    ficherocsv.writeheader()
    # escribir cada fila con los datos
    ficherocsv.writerows(lista)
    fichero.close()
    
crear_csv('data', 'employees.csv', lista_empleados)