#Ejercicios funciones

# 1.- Escribir una función que reciba una muestra de números en una lista y 
# devuelva un diccionario con su media, varianza y desviación típica.

def square(sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

def statistics(sample):
    """Función que calcula la media, varianza y desviación típica de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
    """
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics([1, 2, 3, 4, 5]))
print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

#2.-Escribir una función que calcule el máximo común divisor de dos números y
# otra que calcule el mínimo común múltiplo.

def mcd(n, m):
    """Función que calcula el máximo común divisor de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m.
    """
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

def mcm(n, m):
    """Función que calcula el mínimo común múltiplo de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
    """
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(mcd(24,36))
print(mcm(24,36))

#3.- Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior 
# y devuelva una tupla con la palabra más repetida y su frecuencia.

def count_words(text):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - text: Es una cadena de caracteres.
    Devuelve: 
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

def most_repeated(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(count_words(text))
print(most_repeated(count_words(text)))


#Ejercicios listas y tuplas

# 4.-Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista
# y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for subject in subjects:
    print("Yo estudio " + subject)

# 5.-Escribir un programa que pregunte al usuario los números ganadores de la
# lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

awarded = []
for i in range(6):
    awarded.append(int(input("Introduce un número ganador: ")))
awarded.sort()
print("Los números ganadores son " + str(awarded))

# 6.-Escribir un programa que almacene en una lista los siguientes
# precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))

#Ejercicio diccionarios

# 7.-Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])

#8.- Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre 
# una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario.
#  Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"