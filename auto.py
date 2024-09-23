class Auto:
    #propiedades - atributos - variables
    color = ""
    precio = 0
    combustible = ""
    motorizacion = ""
    matricula = ""
    estado = ""
    
    # metodos - funciones- acciones que puede realizar el objeto
    # funcion constructor no es obligatoria pero me permite inicializar la propiedades del objeto
    def __init__(self, color, precio, matricula, combustible, motorizacion ="100cv"):
        self.color = color
        self.precio = precio
        self.__matricula = matricula
        self.combustible = combustible
        self.motorizacion = motorizacion
        self.estado = 'apagado'
        
    # cuando una funcion modifica una propiedad del objeto se llama setter
    def arrancar(self):
        self.estado = 'Brrrr encendido'

    #getter es una función que me permite sacar valor de una propiedad privada.
    def get_matricula(self):
        return self.__matricula
    

ferrari = Auto('rojo', 75000, '2445-DFG', 'gasolina', '300cv')
fiat = Auto('vino', 1500, 'M-85263-DF', 'diesel', '65cv')

print(ferrari.color)
print(ferrari.get_matricula())
print(fiat.estado)
fiat.arrancar()
print(fiat.estado)