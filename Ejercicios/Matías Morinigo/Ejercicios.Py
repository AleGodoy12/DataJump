#1 Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
# print("!Hola Mundo¡")


#2 Escribir un programa que almacene la cadena !Hola Mundo¡ en una variable y luego muestre por pantalla el contenido de la variable.
#saludo="Hola mundo"3print(saludo)

#3 Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
#horas=float(input("Ingrese las horas trabajadas"))
#precio=float(input("Coste por cada horas"))
#sueldo=horas*precio
#print(sueldo)

#4 Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales
#altura=float(input("Indique su altura"))
#peso=float(input("Indique su peso en kilogramos"))
#indice=peso/(altura**2)
#print("Su indice de peso corporal es:" , indice)

#5  Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total


# pan=3.49
# descuento=60/100
# cantidad=int(input("Indique la cantidad de panes vendidos en el día"))
# coste=pan * descuento
# costeFinal=cantidad * coste
# print(pan , descuento , costeFinal)

# #Ejercicios condicionales
# #1  Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
# Edad=int(input("Ingrese su edad"))
# mayorEdad=18
# if Edad>=mayorEdad: 
#        print("Es mayor de edad") 
# else: 
#     print("No es mayor de edad")       

# #2  Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
# contraseña="1234"
# pregunta=(input("Ingrese la contraseña.. ")).lower()
# if contraseña==pregunta:
#     print("Contraseña correcta")
# else:
#   print("La contraseña es incorrecta")

# #3  Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
# numPedido=int(input("Ingrese un numero.. "))
# modulo= numPedido % 2 
# if modulo==0:
#     print("Es par")
# else:
#      print("Es impar")

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

