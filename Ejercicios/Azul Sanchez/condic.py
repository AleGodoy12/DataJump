# Ejercicios condicionales:

#1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

condicion= 18                              # pongo la condicion para que apartir de ahi me diga si es mayor o menor
edad= int(input("¿Cuántos años tenes? "))  #int: números enteros
if (edad>=18):                             
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# 2.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseña= "Hola123"
contra= input("¿Cuál es su contraseña? ").lower()  # .lower: para q no tenga en cuanta las minúsculas y mayusuclas
if(contra == contraseña):
    print("Contraseña correcta ")
else:
    print("Contraseña incorrecta ")

# 3.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

num=int(input("Ingrese un número: "))
if (num%2==0):                        # num%(modulo)2: si el num es ==o es par sino impar
    print("Es par")
else:
    print("Es impar")

# 4.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

cond= 18                                 # Desicion del precio en funcion de la edad
cond2= 4                                 # las condiciones que me pide el enunciado
precioMayor= "10€"                       # los precios dependiendo la edad
precioMenor= "5€"
precioInfantil= "Gratis"

edad= int(input("Ingrese su edad: "))      # int : numero entero
if (edad>cond)
    print("El precio para la sala de juegos es de:", precioMayor)
else:
    if (edad>=cond2):
        print("El precio de la sala de juegos es de:", precioMenor)
    else:
        print("El precio de la sala de juegos es de:", precioInfantil)

# 5.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre= input("¿Cuál es tu nombre? ")             #input: para pedirle al usuario que ingrese un dato
genero= input("¿Cuál es tu sexo (masculino o femenino)? ")

if genero == "femenino":                         # si el genero es == femenino corresponde al A
    if nombre.lower() < "m":                     # si el nombre es anterior a la m corresponde al A
        grupo= "A"                               # .lower: para q no tenga en cuanta las minúsculas y mayusuclas
    else:
        grupo= "B"                               # de lo contrario va al grupo B
else:
    if nombre.lower() > "n":                       # si el nombre es dsp de la n val al A
        grupo= "A"
    else:
        grupo= "B"                               # de lo contrario al B
print("Te corresponde el grupo: " + grupo)