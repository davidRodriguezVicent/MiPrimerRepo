import pandas as pd

fichero = pd.read_excel('./data/employees.xls', sheet_name="Empleados")
#print( fichero.head() ) # saca la cabecera del documento, los 10 registros
#print(fichero) #impresion completo en un datable

lista_empleados = fichero.to_dict('records')
print(lista_empleados[1]['apellidos'])