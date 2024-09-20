import xml.etree.ElementTree as et
import os

lista_empleados = [
    {'id': 1, 'nombre': 'Juan Antonio', 'apellidos': 'Pérez Jarillo', 'correo': 'jj@gmail.com', 'departamento': 'Desarrollo' },
    {'id': 2, 'nombre': 'Almudena', 'apellidos': 'González Camuñas', 'correo': 'almu@gmail.com', 'departamento': 'Finanzas' },
    {'id': 3, 'nombre': 'Marta', 'apellidos': 'Rodriguez Lopez', 'correo': 'marta@gmail.com', 'departamento': 'Marketing' },
    {'id': 4, 'nombre': 'Joaquin', 'apellidos': 'Calvo Lopez', 'correo': 'joaquin@gmail.com', 'departamento': 'Finanzas' },
    {'id': 5, 'nombre': 'Lucia', 'apellidos': 'Pérez Alvárez', 'correo': 'lucia@gmail.com', 'departamento': 'Cuentas' },
]

raiz = et.Element('empleados') # <empleados></empleados>

# vamos a recorrer el diccionario pintando cada elemento en el mismo xml
for empleado in lista_empleados:
    tag_empleado = et.SubElement(raiz, 'empleado', id= str(empleado['id'])) #<empleado id="1"></empleado>
    for key, value  in empleado.items():
        if key != 'id':
            subtag = et.SubElement(tag_empleado, key) #<correo></correo>
            subtag.text = str(value) #<correo>jj@gmail.com</correo>
            
# crear arbol de xml
xml = et.ElementTree(raiz)
# crear la carpeta donde voy a guardar el elemento
os.makedirs('data', exist_ok=True)
xml.write("data/empleados.xml", encoding='utf-8', xml_declaration=True)
