# *Ejercicios Condicionales*

#1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad= int(input("Escriba su edad por favor: "))
if (edad>18) :
    print ("Usted es mayor de edad")
else :
     print ("Usted no es mayor de edad")
     
     
#2.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.     
uno= input("Ingrese la contraseña")
clave= "contraseña"

if (uno == clave):
    print ("Coincide")
     
     
#3.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
numero= int(input("Escriba un numero: "))

if (numero%2 == 0) :
    print ("es par")
else :
    print ("es impar")
    
#4.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
edades= int(input("Ingrese su edad"))

if (edades >=0 and edades <4 ) :
    print ("Puede entrar gratis")
elif (edades >= 4 and edades <18) :
    print ("Debe pagar €5") 
else :
    (edades >= 18 )
    print ("Debe pagar €10") 
    
5.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre= input("Ingrese su nombre en MAYUSCULA: ")
sexo= input("Ingrese F o M, segun corresponda")

if (sexo == "F" and nombre[0] <="M" or sexo == "M" and nombre[0] >="N") :
    print ("grupo A")
else :
    print ("grupo B")
    