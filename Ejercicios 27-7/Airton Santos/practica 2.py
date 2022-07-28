# 1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).7

from re import I


def mostrarEdad ():
    edad = int(input("Ingrese su edad"))
    edadArr = []
    i = 0
    while i < edad:
        i += 1
        edadArr.append(i)
    return(edadArr)

print(mostrarEdad())

#2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número 
# hasta cero separados por comas


def cuentaRegresiva():
    numero = int(input("Ingrese un número positivo"))
    i = numero
    edadArr = []

    while i >= 0:
        edadArr.append(i)
        i -= 1

    print(edadArr)

cuentaRegresiva()

#3.- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla 
# el capital obtenido en la inversión cada año que dura la inversión.

def gananciasCapital ():
    inversion = int(input("Ingrese cuánto quiere invertir"))
    interes = float(input("Qué interés anual desea?"))
    agnos = int(input("Por cuántos años desea hacer la inversión?"))

    gananciaAnual = (inversion * (interes/100)) + (inversion / agnos)
    print(gananciaAnual)


gananciasCapital()



#4.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

def numerosPrimos():
    numero = int(input("Ingrese un número entero"))
    if (2**(numero -1 )% numero) == 1:
        print("Es primo")
    else:
        print("Es compuesto") 


numerosPrimos()


# 5.- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las 
# letras de la palabra introducida empezando por la última.

def palabraInvertida():
    palabraArr= []
    palabra = input("Ingrese una palabra")
    for letra in palabra:
        palabraArr.append(letra)
    print(palabraArr[::-1])

palabraInvertida()



# 6.- Escribir un programa que muestre todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def programaSalir ():
    palabra = input("Introduzca una palabra")
    while palabra != "salir":
        palabra = input("Introduzca una palabra")

programaSalir()



# 7.- Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
import math

def area ():
    radio = float(input("Ingrese el radio del círculo"))
    return(math.pi * (radio **2))

totalArea = area()

print(totalArea)


def volumen ():
    altura = float(input("Ingrese la altura del cilindro"))
    print(totalArea * altura)

volumen()

# 8.- Escribir una función que reciba un número entero positivo y devuelva su factorial

def factorial():
    numero = int(input("Ingrese un número positivo"))
    i = 0
    fact = 1 

    while i < numero:
        i += 1
        fact *= i
    print(fact)

factorial()

# 9.- Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def media (lista):
    i = 0
    total = 0 
    media = len(lista)

    for i in lista:
        total += i 
    print(total / media)

media([1, 2, 3, 4, 5, 6])

# 10.- Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def saludo ():
    print ("¡Hola amiga!")

saludo()
