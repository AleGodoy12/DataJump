# *Ejercicios Tipo de datos simples:*

# 1.- Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

from importlib import abc


print("¡Hola mundo!")
# 2.- Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
saludo = "¡Hola mundo!"

print(saludo)
# 3.- Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
horasT = int(input("Ingrese la cantidad de horas que trabaja: "))
valorH = int(input("Ingrese el valor de las horas: "))

total = horasT * valorH

print("Lo que recibes por dia es un total de ", total , "$")
# 4.- Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales

peso = float(input("Ingrese su peso: "))
estatura = float(input("Ingrese su estatura: "))

imc = peso/ (estatura*estatura)

print("Tu indice de masa corporal es de: ", str(round(imc)))
# 5.- Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total
panVendido = int(input("Ingrese la cantidad de pan que no era del dia vendido: "))

valorNormal = 3.49

print("El valor del pan del dia es de ", str(valorNormal), "$")

descuento = valorNormal * 60 / 100

print("El descuento por unidad del pan que no es del día es de: ", str(descuento), "$")

total = panVendido * descuento

print("El total del pan comprado es de: ", str(round(total))) 

# *Ejercicios Condicionales*

# 1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad = int(input("Ingrese su edad: ")
)
if (edad >= 18):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
# 2.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseña = ("hellomoto")
contraseñaIngresada =input("Ingrese la contraseña").lower()

if contraseña == contraseñaIngresada:
    print("Conectado")
    
else:
    print("Contraseña incorrecta, intente nuevamente")

# 3.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
numerito = int(input("Escriba un numero y le dire si es par o impar: "))

if numerito % 2 == 0:
    print("Es par")
else: 
    print("Es impar")
# 4.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edadCliente = int(input("Ingrese su edad: "))

if (edadCliente < 4):
    print("Entras gratis")
    
if (edadCliente >= 4 and edadCliente<=18):
    print("Debes pagar 5$")
    
if(edadCliente>18):
    print("Debes abonar 10$ ")
# 5.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre = input("Nombre: ").capitalize() #Para que la primera letra quede en mayúscula
sexo = input("Sexo [M o F]: ").upper()

if(nombre.isalpha and (sexo == "M" or sexo == "F")):
    primeraLetra = nombre[0]
    if(sexo == "F"):
        if(primeraLetra < "M"):
            print("Te toca el grupo A")
        else:
            print("Te toca el grupo B")
    else:
        if(primeraLetra > "N"):
            print("Te toca el grupo A")
        else:
            print("Te toca el grupo B")
else:
    print("Datos inválidos, inténtelo de nuevo.")
# *Ejercicios Bucles*

##1.- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input("Ingresa una palabra cualquiera: ")

i = 0
while(i < 10):
    print(palabra)
    i += 1

# 2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numeroEntero = int(input("Ingrese un número entero que sea positivo: "))
impares = []

if(numeroEntero > 0):
    for impar in range(1, numeroEntero+1):
        if(impar % 2 != 0):
            impares.append(impar) #agrega los impares como el ultimo elemento al array
    print(impares)
else:
    print("Número inválido")

# 3.- Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
multiplicando = int(input("Ingrese un numero: "))

multiplicador = 0

while multiplicador < 10:
    multiplicador += 1
    resultado = multiplicador * multiplicando
    print(resultado)
    
# 4.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contra = "holamundo"

contra2 = ""

while contra2 != contra:
    contra2 = input("Escriba la contraseña ").lower()
print("Contraseña correcta")


# 5.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase


frase = input("Escriba una frase: ")

letra = input("Escriba la letra que desea buscar: ")

aparece = 0

for i in frase:
    if letra == i:
        aparece += 1
print("la letra ", letra ,"aparece: " ,aparece, "en la frase ", frase)