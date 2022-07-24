#Ejercicios Tipo de datos simples:

#1.- Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("hola mundo")

#2.- Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable. 
saludo = "hola mundo"
print(saludo)

#3.- Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde. 
horas=float(input("Ingrese la cantidad de horas trabajadas "))
precio=float(input("Ingrese cuanto cobra por hora "))
sueldo= horas*precio 
print("Su sueldo es: $", sueldo)

#4.- Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
altura=float(input("Ingrese su altura (en metros) "))
peso=float(input("Ingrese su peso (en kilogramos) "))
indice= peso/(altura**2) 
aprox= round(indice, 2)
print("Su indice de masa corporal es: ", aprox)

#5.- Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
barrasDePan = 3.49
cant=int(input("Ingrese cuantas barras NO frescas se vendieron el dia de la fecha "))
precio = cant*barrasDePan
precioConDesc= precio*60/100
aprox= round(precioConDesc, 2)
print("Barras de pan x ", cant )
print("Precio de barra de pan = ", barrasDePan,"€")
print("Descuento del 60%")
print("Total= ", aprox, "€")

#Ejercicios Condicionales

#1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
condicion=18
edad=int(input("Ingrese cuantos años tiene "))
if (edad>=condicion):
    print("Es mayor de edad ")
else:
    print("Es menor de edad ")

#2.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
password="arbusta123456"
contraseña=input("Ingrese la contraseña ").lower() 
if (contraseña==password):
    print("Bienvenido a Arbusta")
else:
    print("Contraseña incorrecta")

#3.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
num=int(input("Ingrese un numero "))
if (num%2==0):
    print("Es par")
else:
    print("Es impar")
    

#4.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
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

#5.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
abecedario = ["a", "b", "c" , "d" , "e" , "f", "g" , "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

primeraParte= abecedario[:12]
segundaParte= abecedario[12:26]

sexo=str(input("Ingrese su sexo biologico (mujer u hombre) ")).lower()
nombre=str(input("Ingrese su nombre ")).lower()

primeraLetra=nombre[0] 

if(sexo=="mujer" and primeraLetra in primeraParte or sexo=="hombre" and primeraLetra in segundaParte):
     print("Bienvenida al grupo A")
else:
    print("Bienvenida al grupo B")

#Ejercicios Bucles

#1.- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra=input("Ingrese una palabra: ")
i=0 #acumulador
while (i<10):
    i += 1
    print(palabra)
print( )

#2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
num=int(input("Ingrese un numero: "))
i=1
while (i<=num):
    print(i)
    i+=2

#3.- Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
multiplicando = 0
multiplicador = 0
while(multiplicando<10):
    multiplicando += 1
    print("Tabla del ", multiplicando)
    while (multiplicador<10):
        multiplicador += 1
        producto = multiplicando * multiplicador
        print(multiplicando, "x", multiplicador, "=" , producto)
    multiplicador -= 10
    print( )
print("Fin del bucle")

#4.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contraseña = input("Cree una contraseña: ")
contra = input("Ingrese su contraseña: ")
while(contraseña!=contra):
    contra = input("Error, ingrese su contraseña nuevamente: ")
print("Bienvenido")


#5.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
from collections import Counter
frase=str(input("Escriba una frase: "))
letra=str(input("Escriba una letra: "))
counter= Counter(frase)
print(counter[letra])





