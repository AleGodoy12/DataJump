# #Ejercicios funciones

# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
listaNum = [12, 23, 17, 21, 19, 7, 11, 9, 13]

def media(lista):
    suma = 0
    for i in lista:
        suma += i
    promedio = suma / len(lista)
    return promedio

#Definición tecnica
# La varianza es una medida de dispersión que representa la variabilidad de una serie de datos respecto a su media. Formalmente se calcula como la suma de los residuos al cuadrado divididos entre el total de observaciones.
def varianza(lista):
    mu = media(lista)
    contador = 0
    for i in lista:
        contador += (i - mu)**2 #(resta el elemento de una lista por la media) = residuo y luego lo eleva al cuadrado
    v = contador / len(lista) #ahora eso lo divide entre el total de observaciones
    return v

def desviacion_tipica(lista): #La desviacion tipica es la raiz cuadrada de la varianza
    raiz_cuadrada = varianza(lista)**0.5 
    return raiz_cuadrada

def matematicas(lista):
    diccionario = {}
    m = media(lista)
    v = varianza(lista)
    dt = desviacion_tipica(lista)
    diccionario.update({"media": m})
    diccionario.update({"varianza": v})
    diccionario.update({"desviacion_tipica": dt})
    return diccionario

resultado = matematicas(listaNum)
print(resultado)

# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.


# #Ejercicios listas y tuplas

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

# #Ejercicio diccionarios

# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.