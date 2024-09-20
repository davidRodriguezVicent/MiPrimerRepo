# Un palindromo es una frase o palabra que se lee igual de derecha a izq que al reves. Sin tener en cuenta los espacios en blanco y ni mayusculas ni minusculas.
# Ana
# Luz azul
# La ruta nos aporto otro paso natural

def is_palindrome(sentence):
    # quitarle los espacio en blanco
    sin_espacios = sentence.replace(" ", "")
    # controlar que la frase esta de la misma forma, toda en minusculas
    minusculas = sin_espacios.lower()
    # invertir la sentencia y compararla con el original
    invertida = minusculas[::-1] #invertir cualquier texto
    return True if invertida == minusculas else False


def main():
    frase = input('Dime un frase o palabra: ')
    resultado = is_palindrome(frase) # es un funcion que tiene como objetivo devolver un True o False
    msg = f'{frase}, es un palindromo' if resultado else f'{frase}, no es un palindromo'
    print(msg)

main()