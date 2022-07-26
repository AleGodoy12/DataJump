#1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad = int(input("Ingresar edad"))
condicion = 18
if (edad>=condicion):
    print("Es mayor")
else: 
    print("Es menor")
    
#2.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
# por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada
# en la variable sin tener en cuenta mayúsculas y minúsculas.
contraseña = "asd12345"
ingreso = input ("Introduzca su contraseña").lower()
if (contraseña == ingreso):
    print(" Bienvenido..")
else:
    print("Datos inválidos, vuelva a intentar")
    
#3.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
num = int(input("Ingrese un numero "))
if (num%2==0):
    print("Es par")
else:
    print("Es impar")
    
#4.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular
# de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar
# al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede 
# entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
cond=18
segundaCond=4
precioMayor= "10€"
precioMenor= "5€"
precioInfantil= "gratuito"

edad=int(input("Ingrese cuantos años tiene "))
if (edad>cond):
    print("El valor de la sala de juegos es de ", precioMayor)
else:
    if (edad>=segundaCond):
        print("El valor de la sala de juegos es de ", precioMenor)
    else:
        print("El valor de la sala de juegos es ", precioInfantil)
        
# 5.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior
# a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre
# por pantalla el grupo que le corresponde.

nombre= input("Ingrese su nombre: ").capitalize()        
genero= input("Ingrese su sexo, si es masculono M, si es femenino F: ").upper()
if genero == "F":                        
    if nombre < "M":                     
        grupo= "A"                               
    else:
        grupo= "B"                               
else:
    if nombre > "N":                       
        grupo= "A"
    else:
        grupo= "B"                               
print("Te corresponde el grupo: " + grupo)