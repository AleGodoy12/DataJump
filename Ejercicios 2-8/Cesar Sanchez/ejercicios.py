# Ejercicios funciones

# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

""" def numeroLista (ingreseLista):

    suma = 0

    cantidad = len(ingreseLista)

    sumatoria = 0

    for i in ingreseLista:

        suma += i

        promedio = suma / cantidad




        numeroMenosPromedio = i - promedio

        elCuadrado = numeroMenosPromedio * numeroMenosPromedio             #Falta

        sumatoria += elCuadrado

        divisionParaVarianza = elCuadrado / sumatoria



    print (promedio) 

    print (divisionParaVarianza) """
      
      


    



# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

""" MCD = El número más grande que divide dos números  """

""" x = int(input("Escriba el primer número: "))

y = int(input("Esceiba el segundo número: "))

def mcd (numero1, numero2):

    numero = 1 

    if x % y == 0:

        return y

    for k in range (int(y/2), 0, -1):

        if x %k == 0 and y % k == 0:

            numero = k

            break """                    #Falta



# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra  función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

""" cadena = str ( input ("Escribir una palabra:")) """



# Ejercicios listas y tuplas

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

""" lista = ["Matemática", "Física", "Química", "Historia", "Lengua"]

for i in range (len(lista)):

  print ("Yo estudio, ", lista [i]) """






# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.




# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios = [ 50, 75, 46, 22, 80, 65, 8]

menor = precios [0]
mayor = precios [0]

for i in precios:

    if i < menor:
        menor = i
    
    elif i > mayor:
        mayor = i

print ("El menor precio es: ", menor)

print("El mayor precio es: ", mayor )





# Ejercicio diccionariosgut

# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.



# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.