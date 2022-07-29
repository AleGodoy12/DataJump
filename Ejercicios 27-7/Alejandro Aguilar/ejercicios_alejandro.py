# 1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Indique su edad: "))
i = 1
while i <= edad:
     print(f"Edad: {i} años")
     i += 1

# 2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas
enteroPositivo = int(input("Ingrese un número positivo: "))
i = []
while enteroPositivo != -1:
     i.append(enteroPositivo)
     enteroPositivo -= 1

print(i)

# 3.- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

cantInvertir = int(input("Ingrese el monto a invertir: "))
interes = int(input("Ingrese el interes anual: "))
años = int(input("Ingrese los años: "))

inver = (cantInvertir * (interes/100) * años) + cantInvertir

print(f"El monto ${cantInvertir} por el interes {interes}% en {años} años es de ${inver}")


# 4.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

numero = int(input("Ingrese un numero entero: "))
list = []
i, a = 1, 0

while i <= numero:
     if(numero % i == 0):
         a += 1
     i += 1
if(a == 2):
     print(f"El {numero} es un numero primo")
else: 
     print(f"El {numero} no es un numero primo")

# 5.- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = input("Ingrese una palabra: ")
a = len(palabra)

while a != 0:
     a -= 1
     print(palabra[a])

# 6.- Escribir un programa que muestre todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def programaSalir ():
    palabra = input("Introduzca una palabra ")
    while palabra != "salir":
        palabra = input("Introduzca una palabra ")

programaSalir()


# 7.- Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función

import math

def area ():
    radio = float(input("Ingrese el radio del círculo "))
    return(math.pi * (radio **2))

totalArea = area()

print(totalArea)


def volumen ():
    altura = float(input("Ingrese la altura del cilindro "))
    print(totalArea * altura)

volumen()

# 8.- Escribir una función que reciba un número entero positivo y devuelva su factorial

num = int(input("Ingrese un numero: "))
def factorial(numero):
     resultado, a= 1, numero
     while a != 0:
         resultado *= a
         a -= 1
     return resultado

factorial1 = factorial(num)
print(f"El factorial de !{num} = {factorial1}")

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


def saludo():
    saludar = "¡Hola amiga!" 
    return saludar

saludo1 = saludo()
print(saludo1)