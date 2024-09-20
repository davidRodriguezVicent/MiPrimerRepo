
def main():
    mi_fichero = open('./data/notas.txt', 'r')
    # read() me sirve para leer un fichero de un tacada
    # readlines() me sirve para leer un fichero linea a linea
    #print(mi_fichero.read())
    # print(mi_fichero.readlines())
    alumnos = []
    for linea in mi_fichero.readlines():
        datos_alumno = linea.split(": ")
        nombre = datos_alumno[0]
        nota = float(datos_alumno[1].replace('\n', ''))
        nuevo_alumno = { 'nombre': nombre, 'nota': nota }
        alumnos.append(nuevo_alumno)
        
    print(alumnos)
    mi_fichero.close()
    
    
    
    
if __name__ == "__main__":
    main()