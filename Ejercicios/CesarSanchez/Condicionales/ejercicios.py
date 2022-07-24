# 1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

""" edad = int (input("Escriba su edad: "))
mayorEdad = 18

if edad >= mayorEdad:
    print ("Es mayor de edad")

else: 
    print ("No es mayor de edad") """

# 2.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

""" contrasenia = str (input("Ingrese la contraseña: "))
contrasenia = contrasenia.lower()

contraseniaVerdadera = "edelp"

if contrasenia == contraseniaVerdadera :
    print ("Contraseña correcta!")
else:
    print ("ERROR!!Contraseña incorrecta") """


# 3.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

""" numeroEntero = int (input("Por favor, introduzca un número: "))

if (numeroEntero % 2 == 0):
    print ("El número ", numeroEntero, " es un número par")

else:
    print ("El número ", numeroEntero, " es un número impar") """


# 4.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

""" edadCliente = int (input("Por favor, cuál es su edad?: "))

if edadCliente <4:
    print ("Hola, no se preocupe. Entra gratis")

elif edadCliente < 18:
    print ("Hola, debe pagar 5€")

else: 
    print("Hola, debe pagar 10€") """

# 5.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.