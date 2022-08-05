#Ejercicios funciones

# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
lista=[20,32,46,24]
def media(lista):
    i=0
    for n in lista:
        i+=n
    media=i/len(lista)
    return media

def varianza(lista):
    i=0
    for n in lista:
        i+=(n-media(lista))**2
    varr= i/len(lista)
    return varr

def desviacionT(lista):
    desviacionT=varianza(lista)**(0.5)
    return desviacionT

def varios(lista):
    varios=dict(media=media(lista),varianza=varianza(lista),desvT=desviacionT(lista))
    return varios
print(varios(lista))

# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
def mcd(a,b):
    c=max(a,b)
    while True:
        if (a%c==0 and b%c==0):
            return c
        c -= 1
        
print(mcd(13,1))

def mcm(a,b):
    c= max(a,b)
    while True:
        if (c % a == 0) and (c % b == 0):
            return c
        c+=1

# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
cadena=("Este es un ejemplo ejemplo ejemplo")

cadena="este es es unn ejemplo es este"
def ej1(cadena):
    nuevo=cadena.split() 
    dicc={}
    for i in nuevo:
        cant= cadena.count(i)
        dicc[i]=cant
    return dicc
print(ej1(cadena))

#Ejercicios listas y tuplas

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
asignaturas=("Matemáticas","Fisica","Química","Historia","Lengua")
print("Yo estudio ",end="")
for asignatura in asignaturas:
    print(asignatura,end=",")
    
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
n=[]
print("Ingresá los 6 numeros ganadores de la loreria primitiva (deben estar entre 1 y el 49, de a uno por favor :) ) ")
while (len(n))<6:
    ingresado=int(input("Ingresa un número: "))
    if (ingresado>0) and (ingresado<=49):
        n.append(ingresado)
    else:
        print("Error!El número debe ser estar entre 1 y 49")
        ingresado=int(input("Ingresa un número entre el 1 y el 49 : "))       
n.sort()
print("Los números que ingresaste son: ",n)

# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
precios=[50, 75, 46, 22, 80, 65, 8]
print("El minimo es:",min(precios),"y el máximo es: ",max(precios))

#Ejercicio diccionarios

# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
datos=dict(nombre=input("Como es tu nombre? "),edad=input("Cuantos años tenés? "),direccion=input("Como es tu dirección? "),telefono=input("Como es tu telefono? "))
print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['direccion']} y su número de teléfono es {datos['telefono']}")

# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, 
# correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
datos={}
nombre=input("Como te llamas? ")
datos['nombre']=nombre
print(datos)

edad=int(input("Cuantos años tenés? "))
datos['edad']=edad
print(datos)

sexo=input("Ingresá tu sexo biológico: ")
datos['sexo']=sexo
print(datos)

telefono=int(input("Ingresá tu número de teléfono: "))
datos['telefono']=telefono
print(datos)

correo=input("Ingresá tu correro electrónico: ")
datos['correo']=correo
print(datos)

color=input("Cuál es tu color favorito? ")
datos['color']=color
print(datos)