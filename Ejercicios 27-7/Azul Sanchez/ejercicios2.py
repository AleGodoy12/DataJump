# 1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad= int(input("¿Cuántos años tenes?" ))
i= 0
for i in range (edad):
    i +=1
    print("Cumpliste " + str(i) + " años")

# 2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas

numero= int(input("Ingrese un número entero positivo: "))
i= 0
for i in range(numero, -1, -1):
    print(i, end=", ")

# 3.- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

invertir= float(input("¿Cuanto desea invertir? "))
interesAnual= float(input("Ingrese el porcentaje de interes anual: "))
años= int(input("¿Cuántos años? "))                               
i= 1
while(i<=años):
    capital= invertir * (interesAnual / 100) * i+invertir
    print("Capital por ", i, "años es de:", capital)
    i += 1

# 4.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

numero= int(input("Ingrese un número entero: ")) 
i= 2
while(numero % i != 0):                                  
    i += 1
if i == numero:
    print(numero, " Es primo ")
else:
    print(numero, " No es primo ")


# 5.- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra= (input("Ingrese una palabra: "))

i= 0
for i in range(len(palabra) -1, -1, -1):
    print(palabra[i])


# 6.- Escribir un programa que muestre todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

frase= input("Escriba algo: ") 
if frase == "salir":
    print("fin")
else:
    frase= input("Escriba algo: ") 


# 7.- Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función

def areaCirculo(radio):
    area= 3.14 * radio **2
    return area

radio1= float(input("¿Cuanto mide el radio de tu circulo?"))
respuesta= areaCirculo(radio1)
print("El area de tu circulo es: ", respuesta)

altura= float(input("¿Cuanto es la altura de tu cilindro?"))
respuesta2= respuesta * altura
print("El volumen de tu cilindro es: ", respuesta2)

# 8.- Escribir una función que reciba un número entero positivo y devuelva su factorial

numero= int(input("Ingrese un numero entero positivo: "))

def factorial(numero):
    resultado= 1
    i= 1
    while i<= numero:
        resultado = resultado * i
        i += 1
    return resultado
print("El factorial de el numero", numero, "es:", factorial(numero),) 

# 9.- Escribir una función que reciba una muestra de números en una lista y devuelva su media.

lista= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def media(lista):
    cantidad= len(lista)
    suma= 0
    for i in lista:
        suma += i
    media= suma/ cantidad
    return media
resultado= media(lista)
print(resultado)


#10.- Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.
 
saludo= input("saludar")
def greet(saludo): 
    print("¡Hola amiga!")
    return 
greet(saludo)
