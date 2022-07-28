# 8.- Escribir una función que reciba un número entero positivo y devuelva su factorial

def factorial(numero):
    resultado = 1
    for i in range(1, numero+1):
        resultado *= i
    return resultado

numero = int(input("Ingresa un número entero positivo: "))
if(numero > 0):
    resultado = factorial(numero)
    print(resultado)
else:
    print("El número no es positivo.")