import os

# ruta del fichero que queremos borrar

def borrar_fichero(nombre_fichero, extension, carpeta):
    ruta = f'./{carpeta}/{nombre_fichero}.{extension}'
    if os.path.exists(ruta):
        ##podemos trabajar con el fichero
        os.remove(ruta)
        print('Fichero eliminado correctamente')
    else:
        print('El fichero no existe')
    
    
borrar_fichero('prueba', 'txt', 'datos')