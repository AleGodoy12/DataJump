# 1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


""" edad = int (input("Escriba su edad: "))

def aniosCumplidos (anios): 
    
    for i in range (1, anios + 1):

        print ("Cumpliste ", i) 

aniosCumplidos(edad)

print( aniosCumplidos) """


# 2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas


""" numeroEnteroPositivo = int (input("Escriba un número entero positivo: "))

lista = [ ]

def numerosPositivos (numero):

    while numero >= 0:

        lista.append(numero)

        numero -= 1
    
    print(lista)

numerosPositivos(numeroEnteroPositivo)

print(numerosPositivos) """





# 3.- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

""" invertir = int (input("Cantidad a invertir: "))
interes = int (input("El interes es: "))
anios = int (input("Años de inversión: "))
d = 365                                         #Días de año
m = 12                                   #Meses del año


def inversion (cantidadInvertir, ganaInteres, tiempoDeposito):

    i = 1

    while i <= anios :
    

        interesMensual = (cantidadInvertir * ( (ganaInteres/100) * (interes/d)  ) ) 

        interesAnual = interesMensual * m * i

        totalGanancia = interesAnual + cantidadInvertir

        print("El capital ", cantidadInvertir, "en un tiempo de ", i , "año, genera una ganacia de: ", round(totalGanancia, 2) )

        i += 1 



inversion(invertir, interes, anios)

print (inversion) """







""" invertir = int (input("Cantidad a invertir: "))
interes = int (input("El interes es: "))
anios = int (input("Años de inversión: "))
i = 365                                         #Días de año
m = 12                                   #Meses del año

def inversion (cantidadInvertir, ganaInteres, tiempoDeposito):

    for c in range(1, anios+1) :

      interesMensual = (cantidadInvertir * ( (ganaInteres/100) * (interes/i)  ) ) 

      interesAnual = interesMensual * m * c

      totalGanancia = interesAnual + cantidadInvertir

      print("El capital ", cantidadInvertir, "en un tiempo de ", c , "año, genera una ganacia de: ", round(totalGanancia, 2) )

inversion(invertir, interes, anios)

print (inversion) """




# 4.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

""" numero = int (input("Ingrese un número entero positivo: "))

def numeroPrimo(num):
    
    contador = 0

    for i in range (1, num+1):

        if num % i == 0:

            contador += 1 
    
    if contador == 2:
        print ("El número: ", num, " es primo")
    
    else:
        print ("El número: ", num, " no es primo")


numeroPrimo(numero)

print(numeroPrimo) """



# 5.- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

""" palabra = str (input("Escriba unja palabra  "))

def reversa (pal):

    for i in range (len(pal)-1, -1, -1 ):

        print(pal[i], end = "")

reversa(palabra)

print(reversa) """







""" palabra = str (input("Escriba unja palabra  "))

def reversa (pal):
    
    resultado = ""                      #Cadena vacía
    cantidad = len (pal)

    while cantidad > 0 :

        resultado += pal [ cantidad - 1 ]   #Posicion menos 1 

        cantidad -= 1

    print (resultado)

reversa(palabra)

print(reversa) """




# 6.- Escribir un programa que muestre todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


""" introduzcaPalabra = str (input("Introduzaca algún caracter: "))

palabraFin = "salir"

def introducir (palabra):

    while palabra != palabraFin :

        palabra = str (input("Introduzaca algún caracter: "))


introducir(introduzcaPalabra)

print(introducir) """



# 7.- Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función


""" diametro = float (input("Introduzca el diametro: "))

radio = round (diametro/2, 2)

pi= 3.14

def circulo (calcular):

    area = pi * (radio * radio)

    volumen =  (4/3) * pi * radio * radio * radio 

    print("El área de su círculo es: ", area)

    print ("El volumen de su círculo es: ", volumen)


circulo (diametro)

print ( circulo) """




# 8.- Escribir una función que reciba un número entero positivo y devuelva su factorial


""" numeroPositivo = int (input("Escriba un número positivo: "))


def factorial (numero):

    producto = 1 

    i = 1 

    while i <= numero:

        producto = producto * i

        i += 1

        
    print("El factorial de ", numero, "! es: ", producto)

factorial (numeroPositivo)

print (factorial) """



# 9.- Escribir una función que reciba una muestra de números en una lista y devuelva su media.


""" lista= [10,20,40,80 ]

cantidad= len(lista)

def media(list):
    
    sumaLista= 0
    
    for i in list:
    
        sumaLista += i
    
    media = sumaLista / cantidad
    
    print ("La media es: ", media)

media(lista)

print(media) """






# 10.- Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

""" def saludar (): 
    saludo = "!Hola amiga¡"

    print (saludo)

saludar()
print(saludar) """