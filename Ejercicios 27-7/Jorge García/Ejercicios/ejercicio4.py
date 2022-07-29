# 4.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

numero = int(input("Ingresa un número entero: "))

if(numero > 1):
    esPrimo = True
    for i in range(2, numero):
        if(numero % i == 0):
            esPrimo = False
            print(f"El número {numero} no es primo")
            break
    if(esPrimo):
        print(f"El número {numero} es primo")
else:
    print("El número ingresado no puede ser primo.")