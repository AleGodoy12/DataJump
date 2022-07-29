# 1.- Escribir un programa que pregunte al usuario su edad y muestre 
# por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# age = int(input("¿Cuántos años tienes? "))
# for i in range(age):
#     print("Has cumplido " + str(i+1) + " años")

# 2.- Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla la cuenta atrás desde ese número hasta 
# cero separados por comas

# n = int(input("Introduce un número entero positivo: "))
# for i in range(n, -1, -1):
#     print(i, end=", ")

# 3.- Escribir un programa que pregunte al usuario una cantidad 
# a invertir, el interés anual y el número de años, y muestre por pantalla 
# el capital obtenido en la inversión cada año que dura la inversión.

# amount = float(input("¿Cantidad a invertir? "))
# interest = float(input("¿Interés porcentual anual? "))
# years = int(input("¿Años?"))
# for i in range(years):
#     amount *= 1 + interest / 100 
#     print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2))

# 4.- Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla si es un número primo o no.

# n = int(input("Introduce un número entero positivo mayor que 2: "))
# i = 2
# while n % i != 0:
#     i += 1
# if i == n:
#     print(str(n) + " es primo")
# else:
#     print(str(n) + " no es primo")

# 5.- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
# una a una las letras de la palabra introducida empezando por la última.

# word = input("Introduce una palabra: ")
# for i in range(len(word)-1, -1, -1):
#     print(word[i])

# 6.- Escribir un programa que muestre todo lo que el usuario introduzca 
# hasta que el usuario escriba “salir” que terminará.

# while True:
#     frase = input("Introduce algo: ")
#     if frase == "salir":
#         break
#     print(frase)

#7.- Escribir una función que calcule el área de un círculo 
#y otra que calcule el volumen de un cilindro usando la primera función

# def circle_area(radius):
#     """Función que calcula el area de un círculo.
#     Parámetros
#     radius: Es el radio del círculo.
#     Devuelve el área del círculo de radio radius. 
#     """
#     pi = 3.1415
#     return pi*radius**2

# def cilinder_volume(radius, high):
#     """Función que calcula el volumen de un cilindro.
#     Parámetros
#     radius: Es el radio de la base del cilindro.
#     high: Es la altura del cilindro.
#     Devuelve el volumen del clindro de radio radius y altura high.
#     """
#     return circle_area(radius)*high

# print(cilinder_volume(3,5))

#8.- Escribir una función que reciba un número entero positivo y devuelva su factorial
# def factorial(n):
#     """Función que calcula el factorial de un número entero positivo.
#     Parámetros
#     n: Es un entero positivo.
#     Devuelve el factorial de n.
#     """
#     tmp = 1
#     for i in range(n):
#         tmp *= i+1
#     return tmp

# print(factorial(4))
# print(factorial(20))

#9.- Escribir una función que reciba
#una muestra de números en una lista y devuelva su media.

# def mean(sample):
#     """Función que calcula la media de una muestra de números.
#     Parámetros
#     sample: Es una lista de números
#     Devuelve la media de los números en sample. 
#     """
#     return sum(sample)/len(sample)

# print(mean([1, 2, 3, 4, 5]))
# print(mean([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

#10.- Escribir una función que muestre por pantalla 
#el saludo ¡Hola amiga! cada vez que se la invoque.

# def greet():
#     """Función que muestra el saluco ¡Hola amiga! por pantalla."""
#     print('¡Hola amiga!')
#     return

# greet()