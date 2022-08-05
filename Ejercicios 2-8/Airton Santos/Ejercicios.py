# #1. Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

dic1 = {}


def calculos(lista):

    media = 0 
    media = sum(lista) / (len(lista))

    for valor in lista:

        varianzaNum = 0 
        varianzaNum += (valor - media)**2

    varianzaResultado = varianzaNum / (len(lista))

    print (media, varianzaNum, varianzaResultado)



calculos([1500 , 1200 , 1700 , 1300 , 1800])





# #3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. 

dic2 = {}

def dicPalabras (cadena):

    palabras = cadena.split()

    for i in palabras:
        contador = palabras.count(i)
        dic2[i] = contador
    return dic2

print(dicPalabras("Hola cómo estás Hola Hola Hola"))
resultadoDic = dicPalabras("Hola cómo estás Hola Hola")

# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def tupla ():

    maximoValor = max(resultadoDic, key = resultadoDic.get)

    print(maximoValor)
tupla()   



# #Ejercicios listas y tuplas

# #Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# # en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

def asignaturas (lista):
    for asignatura in lista:
        print(f"Yo estudio {asignatura}")

asignaturas(["Matemáticas", "Física", "Química", "Historia"])

# #Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# # los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. --> Se puede complejizar usando un if, para validar nros.

def loteriaPrimitiva ():
    i = 0 
    lista = []
    while i < 6:
        numeros = int(input("Ingrese un número del 1 al 49"))
        lista.append(numeros)
        lista.sort()
        i += 1 
    print(lista)

loteriaPrimitiva() 

# #Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre
# #  por pantalla el menor y el mayor de los precios.

def precios ():
    listaPrecios = [50, 75, 46, 22, 80, 65, 8]

    precioMaximo = max(listaPrecios)
    precioMinimo = min(listaPrecios)

    print(f"El mayor precio es {precioMaximo}")    print(f"El menor precio es {precioMinimo}")

precios()

# #Ejercicio diccionarios

# # Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después 
# # debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

def infoUsuario ():

    nombre = input("Ingrese su nombre")
    edad = int(input("Ingrese su edad"))
    direccion = input("Ingrese su dirección")
    telefono = int(input("Ingrese su telefono"))

    dic2 = {"Nombre": nombre, "Edad": edad, "Direccion": direccion, "Teléfono": telefono}


    print(dic2["Nombre"], " tiene ", dic2["Edad"], " años, vive en ", dic2["Direccion"], " y su número de teléfono es ", dic2["Teléfono"])

# infoUsuario()

# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

def programaUsuario():

    dic4 = {}
    i = 0

    while i < 3:
        nombre = input("Ingrese su nombre")
        dic4["Nombre"] = nombre
        print(dic4)
        i += 1

        edad = int(input("Ingrese su edad"))
        dic4["Edad"] =dad
        print(dic4)
        i += 1

        telefono = int(input("Ingrese su telefono"))
        dic4["Telefono"] = telefono
        print(dic4)
        i += 1

programaUsuario()