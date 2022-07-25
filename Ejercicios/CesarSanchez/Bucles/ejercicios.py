# *Ejercicios Bucles*

# 1.- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

""" palabra = str (input("Introduzca una palabra: "))

for i in range(10):
    print(palabra) """

# 2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

""" numero = int (input("Ingrese un número: "))
numeroInicio = 0
contadorImpares = []

for i in range (1, numero, 1):

    if numero % 2 == 0:
        numeroInicio += 1
        print (numeroInicio)
    
    else: 
        print(numeroInicio) """
    

    
# 3.- Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10

""" numero = int (input("Ingrese un número: "))

for i in range (1, 11):
    
    multiplicacion = i * numero 
    
    print("La multiplicaión de ", numero, " * ", i, " = ", multiplicacion)  """

# 4.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

""" contrasenia = str (input("Ingrese su contraseña: "))

contraseniaCorrecta = "EDELP"

while (contrasenia != contraseniaCorrecta):

    print ("contraseña erronea ")

    contrasenia = str (input("Introduzca su contraseña: "))

if (contrasenia == contraseniaCorrecta):
    print("Contraseña correcta") """


# 5.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase

""" frase = input ("Ingrese una frase: ")
substring = "a"

ocurrencias = frase.count(substring)

print ("El número de veces que se repite la letra ", substring, " es: ", ocurrencias) """