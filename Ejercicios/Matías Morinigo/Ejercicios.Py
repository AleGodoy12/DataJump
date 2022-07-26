#1 Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
from ast import For


print("!Hola Mundo¡")


#2 Escribir un programa que almacene la cadena !Hola Mundo¡ en una variable y luego muestre por pantalla el contenido de la variable.
saludo="Hola mundo"
print(saludo)


#3 Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
horas=float(input("Ingrese las horas trabajadas"))
precio=float(input("Coste por cada horas"))
sueldo=horas*precio
print(sueldo)


#4 Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales
altura=float(input("Indique su altura"))
peso=float(input("Indique su peso en kilogramos"))
indice=peso/(altura**2)
print("Su indice de peso corporal es:" , indice)


#5  Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total
pan=3.49
descuento=60/100
cantidad=int(input("Indique la cantidad de panes vendidos en el día"))
coste=pan * descuento
costeFinal=cantidad * coste
print(pan , descuento , costeFinal)


#Ejercicios condicionales
#1  Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
Edad=int(input("Ingrese su edad"))
mayorEdad=18
if Edad>=mayorEdad: 
       print("Es mayor de edad") 
else: 
    print("No es mayor de edad")       


#2  Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
contraseña="1234"
pregunta=(input("Ingrese la contraseña.. ")).lower()
if contraseña==pregunta:
    print("Contraseña correcta")
else:
  print("La contraseña es incorrecta")


#3  Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
numPedido=int(input("Ingrese un numero.. "))
modulo= numPedido % 2 
if modulo==0:
    print("Es par")
else:
     print("Es impar")


#4 Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
Edad=int(input("Ingrese la edad del cliente"))
mayorEdad=18
entrada=5
if Edad<4:
    print("Puede ingresar gratis")
elif Edad>4 and Edad<18:
    print("Debe pagar 5")
elif Edad>18:
    print("Debe pagar 10")

#5- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
mujeres = ("A","B","C","D","E","F","G","H","I","J","K","L","M")
hombres = ("N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")
nombre=input("Ingrese su nombre ").capitalize()
genero=input("Masculino o femenino ").capitalize()
if (nombre.startswith(mujeres) and genero=="Femenino"):
    print("Iras en el gruppo A")
elif (nombre.startswith(hombres) and genero=="Masculino"):
    print("Iras en el grupo A")
else:
    print("Iras en el grupo B")


#Ejercicios bucle
#1 Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabPedida=input("Ingrese una palabra ")
print(palabPedida*10)

#2 Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
numEntero=int(input("Mande un num entero positivo"))
numero=0
while(numero < numEntero):
    numero += 1
    if numero % 2 == 1:
      print(numero)

#3 Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
tabla=int(input("Nombre una tabla de multiplicar "))
i=0
while(i<10):
    i += 1
    resultado = tabla * i 
    print(resultado)

#4  Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contraseña="1234" #Contraseña correcta 
pregunta=input("Ingrese la contraseña.. ").lower() 
i=0
while(contraseña!=pregunta): #Se ejecuta si no es coinciden el numero que ingreso el usuario
    pregunta=input("intente nuevamente ") #Se mostrara de nuevo tras la respuesta incorrecta del usuario
print("Accediendo al sistema")

 #5 Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase
fraIngresada=input("Ingrese una frase")
letIngresada=input("Ingrese una letra")
contador=0
E=0
while E<len(fraIngresada):
    if fraIngresada[E]==letIngresada:
        contador+=1
    E+=1
print(contador)
   
