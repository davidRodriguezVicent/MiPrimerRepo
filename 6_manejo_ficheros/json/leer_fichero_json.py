import json as js

def leer_fichero(carpeta, nombre_fichero):
    fichero = open(f'{carpeta}/{nombre_fichero}', 'r')
    backup_data = js.load(fichero);
    fichero.close()
    return backup_data


datos = leer_fichero('data', 'empleados.json')
print(datos[3]['nombre'])