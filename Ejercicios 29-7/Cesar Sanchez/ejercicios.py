# 1.- Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5


""" x = 0

numeroLimite = 15

def incremento (numero):

    while numero <= numeroLimite:

        print (numero)
        numero += 5


incremento(x) """

                                       
                                       
                                       
                                       
                                       
                                       # A tener en cuenta 

""" def incremento ():          
    
    x = 0

    numeroLimite = 15

    while x <= numeroLimite:

        print (x)

        x += 5
          

print(incremento()) """                """ NO NECESITO VOLVER HACER PRINT PORQUE ADENTRO DE LA FUNCIÓN porque YA LO EJECUTÉ. 
                                            DE LO CONTRARIO ME IMPRIMIRÁ "NONE" como en este caso. Imprime al final NONE """





# 2.- Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.

""" x = int (input ("Escribir un número positivo: "))
numeroLimite = -100

def decremento (numero):

    while numero >= numeroLimite:

        print(numero)

        numero -= 20
    
decremento(x) """




# 3.- Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecución esta frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'...

""" x = int (input("Escribir un número positivo: "))

valorLimite= 0

def decremento (numero):

    while numero >= valorLimite:

      print("El valor del bucle es: ", numero)

      numero -=1

decremento(x) """






# 4.- Crea un bucle for que itere la siguiente tupla y muestre una frase como esta en cada iteración: 'El color es: ' + color + '.'

""" lista = ["Rojo","Negro", "Blanco", "Celeste"]

def iteracion (colores):

    for i in colores:

        print("El color es: ", i)



iteracion(lista) """




# 5.- Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100. Basta con que imprimas el valor de cada iteración.

""" x = 7
valorLimite = 700 

def iteracion (numero):

    for i in range (numero, valorLimite, 100):
        print (i)

iteracion(x) """



# -Opcional-

# **Crea un bucle while con las siguientes características:
# El valor inicial de la variable x será de 0.                
# El valor de incremento será 1.                               
# La condición de salida del bucle será mayor o igual a 30.    
# La ejecución se deberá romper cuando x valga 15.   break x = 15 
# Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
# Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
# En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
# Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 'Se rompió la ejecución del bucle cuando x valía ' + x **

x = 0
valorLimite = 30 

def opcional (numero):

    while numero <= valorLimite:

        if (numero == 4 or numero == 6 or numero == 10 ):

            print ("Se saltó el valor de : ", numero)

        else: 
            print ("El valor del bucle es: ", numero)

        numero +=1

    
        if (numero == 15):

            print ("Se rompió la ejecución cuando valía: ", numero)
            
            break                                                      # Se usa para cortar la ejecución 

opcional(x)
        

