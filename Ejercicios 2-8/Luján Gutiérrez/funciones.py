#FUNCIONES
#1 Escribir una función que reciba una muestra de números en una lista y devuelva 
# un diccionario con su media, varianza y desviación típica.
dicc = {}
lista = []
def calculos (lista):
    suma = sum(lista)
    longitud = len(lista)
    media = suma / longitud
    varianza = (media / i)


#2 Escribir una función que calcule el máximo común divisor de dos números y otra que 
# calcule el mínimo común múltiplo.

num = 1
num2 = 2
def mcd (a, b):
    i=0
    while True:
        if (i%a==0 and i%b==0):
            return i
    i  += 1

def mcm (a, b):
    c = min(a,b)
    while c>=1:
        if (a%c==0 and b%c==0):
            return c
        c -=  1

print (mcd())
print (mcm())


#3 Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada
#  palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado 
# con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

texto = ["Esto", "es", "una", "lista"]
dicc={}

for i in texto:
    valor = texto.count(i)
    dicc.update({i:valor})
print(dicc)


#EJERCICIOS Y TUPLAS

#4 Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y 
# la muestre por pantalla el mensaje Yo estudio , donde es cada una de las asignaturas de la lista.
materias = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
for i in materias:
    print('Yo estudio', i, 'en la posición' , materias.index(i))


# 5 Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
numGanadores = int(input('Decime los 6 números ganadores de la lotería'))






