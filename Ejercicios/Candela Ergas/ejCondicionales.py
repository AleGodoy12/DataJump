# *Ejercicios Condicionales*

# 1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

from locale import normalize


edad= int(input("Ingresá tu edad "))
eMayor= 18

def mayor(edad,eMayor):
    if edad >= eMayor:
        print("Sos mayor de edad")
    else:
        print("Todavia no sos mayor de edad </3")

mayor(edad,eMayor)


# 2.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña
#  e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas 
#  y minúsculas.

contraseña="holA1"
contraseñaUser=str(input("Ingresá la contraseña "))

if (contraseña.lower()) == (contraseñaUser.lower()):
    print("Acceso permitido")
else: 
    print("Las contraseñas no coinciden,intentá de nuevo")


# 3.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numUser= int(input("Ingresá un numero "))
if (numUser%2 == 0):
    print("Es un número par!")
else:
    print("Es un número impar")



# 4.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio
#  que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
#  Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad = int(input("Cuántos años tenés? "))
if edad <4:
    print("Podés pasar gratis ^.^")
elif edad>=4 and edad<18:
    print("El precio de tu entrada es 5€")
else:
    print("El precio de tu entrada es 10€")

# 5.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres 
# con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al 
# usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre=str (input("Ingresá tu nombre: ")).capitalize()
sexo=str(input("Ingresá tu sexo biológico, F ó M: ")).upper()
datosOk= nombre.isalpha and (sexo=="F" or sexo=="M")
inicial=nombre[0]

if (datosOk):
    if (sexo=="F" and inicial<"M") or (sexo=="M" and inicial>"N"):
        print("Estás en el grupo A")
    else:
        print("Estás en el grupo B")
else:
    print("Datos erroneos, volvé a intentar")