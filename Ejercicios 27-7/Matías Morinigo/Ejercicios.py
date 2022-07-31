# 1 Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input("Cuantos años tiene: "))
for contador in range(edad):
   print("Cumpliste " + str(contador+1) + " años")

age = int(input("¿Cuántos años tienes? "))
for i in range(age): # i es un contador # range  del objeto
   print("Has cumplido " + str(i+1) + " años") # string es el tipo de dato 


# 2 Escribir un programa que pida al usuario un número entero positivo y muestre 
#por pantalla la cuenta atrás desde ese número hasta cero separados por comas
num = int(input("Ingrese un numero entero positivo: "))
i = 0
for i in range(num):
   print(num-i)


# 3  Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de 
#años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
cantInver = float(input("Ingrese la cantidad a invertir: "))
interAnual = float(input("Ingrese el interes anual: "))
numAños =  int(input(" Escriba el numero de años: "))
i = 1
while (i<=numAños):
    capital = cantInver*(interAnual/100)*i + cantInver
    print("El capital del ", i , "año es de: ", capital)
    i+=1


# 4  Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
numEntero = int(input("Ingrese un numero entero: "))
i = 2
for numEntero in range(i , numEntero):        #! no debe usarse    #return si el primer print es falso 
    if (numEntero % i ==0):                                        #While sirve para comparar 
        print(numEntero, " No es primo")                           ##For muestra en lista 
    else: 
        print(numEntero, " Es primo")

n = int(input("Introduce un número entero positivo mayor que 2: ")) #Ej: 13
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
     print(str(n) + " no es primo")


# 5 Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a 
# una las letras de la palabra introducida empezando por la última.
pala = input("Ingrese una palabra: ")              #-1,-1,-1 ordena hacica atras
for i in range(len(pala)-1, -1, -1):               
    print(pala[i])

pala = input("Ingrese una palabra")
for i in reversed(pala):
    print(i)


# 6 Escribir un programa que muestre todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
while True:
    palaIntro = input("Introduzca un mensaje: ")                   #== comparar, = asignar variable 
    if palaIntro == "salir":                                       #Break interrumpe el bucle 
        break
    print(palaIntro)

bar = True                                                        #2da forma de hacerlo sin el Break
while bar:
    intro = input("Introduzca una palabra: ")
    if intro == "salir":
        bar = False
    print(intro)

# 7 - Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función
radio = int(input("Indique el radio de un cilindro: "))
altura = int(input("Indique la altura: "))

import math 

# area = math.pi*(radio**2)
# print(area)

# volumen = area * altura
# print(volumen)

def capacidad(radio):
    area = math.pi*(radio**2)
    return area 
def tamaño(altura,radio):
    area = capacidad (radio)
    volumen = area * altura 
    return volumen 
tam = tamaño(altura , radio)
print(tam)


# 8  Escribir una función que reciba un número entero positivo y devuelva su factorial
numPosi = int(input("Escriba un numero entero positivo: "))
from math import factorial                         
def num(numPosi):
    rando = "La factorial es: ", factorial(numPosi)
    return rando
rum = num (numPosi)
print(rum)

# 9  Escribir una función que reciba una muestra de números en una lista y devuelva su media.
lista = [20, 47, 70, 83, 25]
i = 0 
san = 0
for num in lista: 
    i += 1
    san += num
print(san / i)

def promedio(lista):
    i = 0 
    san = 0 
    for num in lista: 
     i += 1
     san += num
    return san/i
namber = promedio(lista)
print(namber) 


# 10  Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.
hello = "Hola amig@"
print(hello)
def hola():
    hello = "Hola amig@"
    return hello
hi = hola()
print(hi)