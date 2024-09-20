
def update_file(nombre_fichero, carpeta):
    mi_fichero = open(f'./{carpeta}/{nombre_fichero}', 'a', encoding='utf-8')
    nombre = input('Dime un nombre: ')
    nota = input('Dime una nota: ')
    mi_fichero.write(f'{nombre}: {nota}\n')
    
    mi_fichero.close()
    
    
update_file('notas.txt', 'data')