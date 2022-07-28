# # 1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# edadUsuario = int(input("Ingrese su edad actual: "))
# for i in range(edadUsuario):
#     print("Ya cumpliste " + str(i+1) + " años")


# # 2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas

# numeroEntero= int(input("Ingrese un numero entero que sea positivo: "))

# for i in range( -1, numeroEntero):
#     print(i+1, end=", ")

# 3.- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
# inversion =float(input("Ingrese la cantidad de dinero que desea invertir: "))
# interesAnual = float(input("Ingrese el interes anual: "))
# años = int(input("Ingrese la cantidad de años: "))

# for i in range(años):
#     inversion *=1 + interesAnual / 100
# print() 

# 4.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
# numerosPrimos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# ingresado = int(input("Ingrese un numero: "))

# if numerosPrimos== ingresado:
#     print("Es un numero primo")
# else:
#     print("No es un numero primo")

# 5.- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

# palabra= input("Ingrese una palabra: ")

# for i in range( palabra):
#     print(i+1, end=", ")


# 6.- Escribir un programa que muestre todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

while True:
    algo = input("Escriba una frase:")
    if (algo == "salir"):
        break


# 7.- Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función

def areaCirculo(radio):
    return 3,14* (radio*radio)

print("El area del circulo es de ", str(areaCirculo(4)))

def volumenCilindro(altura):
    return areaCirculo() * altura
print("El volumen del cilindro es de ", str(volumenCilindro(16)))
# 8.- Escribir una función que reciba un número entero positivo y devuelva su factorial
def factorial_normal(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1
    return r

# 9.- Escribir una función que reciba una muestra de números en una lista y devuelva su media.
from statistics import mean
lista = [10, 10, 15, 25, 20]
def mediaLista(*lista):
    return sum(lista)/len(lista)
print(mean(lista))

# 10.- Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def saludito():
    print("¡Hola amiga!")
print(saludito())