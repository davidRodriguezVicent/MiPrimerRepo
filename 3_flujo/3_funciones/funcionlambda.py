# al funcion lambda son funciones abreviadas, estan pensada para reducir la indentación de codigo cuando sea necesario.

def getNameComplete(name, surname):
    return f"{name} {surname}"


nombre_completo = getNameComplete('Juan', 'Perez')
print(nombre_completo)

# funcion lambda

getNameCompleteLambda = lambda name, surname : f"{name} {surname}"
nombre_completo2 = getNameCompleteLambda('Ana', 'Guitierrez')

sumar = lambda n1,n2 : n1+ n2
print(sumar(1,2))