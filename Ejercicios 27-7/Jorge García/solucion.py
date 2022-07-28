# 1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos 
# los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Edad: "))

if(edad > 0):
    for edad in range(1, edad+1):
        print(edad)
else:
    print("Edad inválida")

# 2.- Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas

numero = int(input("Ingresa un número positivo: "))
texto = ""
if(numero > 0):
    for i in range(numero, -1, -1):
        if(i == 0):
            texto += f"{i}."
        else:
            texto += f"{i}, "
    print(texto)
else:
    print("Ojo! No es un número positivo.")

# 3.- Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.

inversion = float(input("Ingresa la cantidad que quieres invertir: "))
tasaInteres = float(input("Ingresa la tasa de interés anual [10 por ejemplo]: "))
tiempo = int(input("Ingresa los años que durará la inversión: "))

if(int(inversion) > 0 and int(tasaInteres) > 0 and int(tasaInteres) <= 100 and tiempo > 0):
    tasaInteres = tasaInteres / 100
    for anio in range(0, tiempo):
        ganancia = round(inversion * tasaInteres * 12, 2)
        capital = inversion + ganancia
        print(f"\nAño {anio+1} - Capital total obtenido: {capital}$ - Ganancia: {ganancia}$ - Inversión: {inversion}$")
        inversion = capital
else:
    print("Datos inválidos, intentalo más tarde.")

# 4.- Escribir un programa que pida al usuario un número entero 
# y muestre por pantalla si es un número primo o no.

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

# 5.- Escribir un programa que pida al usuario una palabra y 
# luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = input("Ingresa una palabra: ")
indice = len(palabra)-1
while indice >= 0:
    print(palabra[indice])
    indice -= 1

# 6.- Escribir un programa que muestre todo lo que el usuario 
# introduzca hasta que el usuario escriba “salir” que terminará.

texto = ""
while(texto != "salir"):
    texto = input("Escribe lo que quieras: ")

# 7.- Escribir una función que calcule el área de un círculo y otra que calcule
#  el volumen de un cilindro usando la primera función

import math

def calcularAreaCirculo(radio):
    area = math.pi * radio**2
    return round(area, 3)

def calcularVolumenCilindro(radio, altura):
    area = calcularAreaCirculo(radio)
    volumen = area * altura
    return volumen

radio = 9
areaCirculo = calcularAreaCirculo(radio)
altura = 14
volumenCilindro = calcularVolumenCilindro(radio, altura)
print(f"El área del circulo es: {areaCirculo}")
print(f"El volumen del cilindro es: {volumenCilindro}")

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

# 9.- Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def calcularMedia(listaNumeros):
    if(len(listaNumeros) > 0):
        acumulador = 0
        for numero in listaNumeros:
            acumulador += numero
        return round(acumulador/len(listaNumeros), 3)
    return 0

lista = [10, 50, 34, 130, 2, 67]
media = calcularMedia(lista)
if(media != 0): 
    print(media)
else:
    print("Lista vacía.")
    
# 10.- Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def saludar():
    return "¡Hola amiga!"

print(saludar())
print(saludar())
print(saludar())
print(saludar()) 