#1.- Escribir un programa que pregunte al usuario su edad y 
# muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad= int(input("Indicame tu edad: "))
i= 0
while i<edad :
    i+= 1
    print ("Cumplió: ", i)
    
# 2.- Escribir un programa que pida al usuario un número entero positivo
# y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas

numero= int(input("Escriba un número"))
i = numero
while i>=0 :
    print (i, end=" , ")
    i -= 1
    
#3.- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de 
# años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

cantidad= float(input("Ingrese cantidad a invertir: "))
interes= float(input("Ingrese el porcentaje de interes anual: "))
años= int(input("Cantidad de años: "))
i= 1
while i<= años :
    capital= cantidad+cantidad*(interes /100) * i
    i += 1
    print ("Tu capital es de", capital)
    
    
# 4.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es 
# un número primo o no.

numero= int(input("Escriba un numero mayor que 2: "))
numero2= 2
while numero % numero2 != 0:
        numero2 += 1
if numero2 == numero :
        print  ("es numero primo")
else :
    print ("no es primo")
    
#5.- Escribir un programa que pida al usuario una palabra y luego muestre
# por pantalla una a una las letras de la palabra introducida empezando por la última.

#6.- Escribir un programa que muestre todo lo que el usuario introduzca 
#hasta que el usuario escriba “salir” que terminará.

palabra= input("Escriba una palabra, hasta hallar la correcta")
palabraCorrecta= "salir"

while palabra != palabraCorrecta :
    palabra= input("Escriba una palabra, hasta hallar la correcta")
    
    