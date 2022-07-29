#Condicionales

#1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Ingrese su edad: "))

if(edad >= 18):
    print("Sos mayor de edad")
else:
    print("Sos menor")
    
    
#2.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseña = "holamundo123"

ingreseC = input("Ingrese la contraseña: ").lower()

if(contraseña == ingreseC):
    print("Conectado")
else:
    print("Contraseña incorrecta, ingrese nuevamente")
    
#3.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numeroEntero = int(input("Ingrese un numero: "))

if(numeroEntero % 2 == 0):
    print("El número ingresado es par")
else:
    print("El número ingresado es impar")
    
#4.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edadCliente = int(input("Ingrese su edad: "))

if(edadCliente <= 4):
    print("Ingresas gratis a la sala de juegos")
if(edadCliente >= 4 and edadCliente <=18):
    print("El valor para ingresar a las salas es de: 5€")
if(edadCliente > 18):
    print("El valor para ingresar a las salas es de: 10€")
    
#5.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

abc = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z")

grupoUno= abc[:12]
grupoDos= abc[12:26]

nombre = (input("Ingrese su nombre: ")).lower()        #Lower convierte mayuscula en minuscula
sexo = (input("Ingrese su sexo (femenino/masculino): ")).lower()

inicial = nombre[0] 

if(sexo == "femenino" and inicial in grupoUno or sexo == "masculino" and inicial in grupoDos):
     print("Bienvenida al grupo A")
else:
    print("Bienvenida al grupo B")
    

