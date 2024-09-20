#Quiero que pidais un numero por pantalla y me saqueis el factorial de dicho numero
# 5 -> 5*4*3*2*1 = 120 

def main():
    resultado = 1
    cadena = ""
    numero = int(input('Dime un numero para calcular el factorial: '))
    while numero >= 1:
        resultado *= numero #resultado = resultado * numero
        if numero != 1:
            cadena = cadena + str(numero) + " x "
        else:
            cadena = cadena + str(numero) + " = "
        numero -= 1
    cadena = cadena + str(resultado)
    print(cadena)
    

main()