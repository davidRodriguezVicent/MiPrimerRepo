class Calculadora:
    # como no tengo que inicializar ni variables ni metodos no necesito la funcion __init__ constructor
    def sumar(self, *numeros):
        suma = 0
        for numero in numeros:
            suma += numero
        return suma
    
    def restar(self, n1, n2):
        return n1 - n2 if n1 >= n2 else n2 - n1
    
    def multiplicar(self, n1, n2):
        return n1 * n2