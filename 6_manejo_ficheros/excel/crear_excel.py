import os
from openpyxl import Workbook

lista_empleados = [
    {'id': 1, 'nombre': 'Juan Antonio', 'apellidos': 'Pérez Jarillo', 'correo': 'jj@gmail.com', 'departamento': 'Desarrollo' },
    {'id': 2, 'nombre': 'Almudena', 'apellidos': 'González Camuñas', 'correo': 'almu@gmail.com', 'departamento': 'Finanzas' },
    {'id': 3, 'nombre': 'Marta', 'apellidos': 'Rodriguez Lopez', 'correo': 'marta@gmail.com', 'departamento': 'Marketing' },
    {'id': 4, 'nombre': 'Joaquin', 'apellidos': 'Calvo Lopez', 'correo': 'joaquin@gmail.com', 'departamento': 'Finanzas' },
    {'id': 5, 'nombre': 'Lucia', 'apellidos': 'Pérez Alvárez', 'correo': 'lucia@gmail.com', 'departamento': 'Cuentas' },
]


def crear_excel(carpeta, fichero, lista):
    # crear el libro de excel a través de la libreria Workbook
    libro = Workbook()
    # seleccionamos una hoja del libro
    hoja = libro.active
    hoja.title = "Empleados"
    
    campos = []
    for key in lista[0].keys():
        campos.append(key)
    hoja.append(campos)
    
    #insertar los valores de cada uno de los registros
    for empleado in lista:
        hoja.append([
                     empleado['id'],
                     empleado['nombre'],
                     empleado['apellidos'],
                     empleado['correo'],
                     empleado['departamento']
                    ])
    os.makedirs(carpeta, exist_ok=True)
    libro.save(f'{carpeta}/{fichero}')
    
crear_excel('data','employees.xls', lista_empleados)