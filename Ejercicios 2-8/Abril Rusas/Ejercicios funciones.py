# #Ejercicios funciones

#1. Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
def media(array):
    cant=len(array)
    suma=0
    for i in array:
        suma+=i
    media=suma/cant
    return media

def varianza(array):
    numerador=0
    for i in array:
        numerador+=(i-media(array))**2
    varianza=numerador/len(array)
    return varianza

def desviacionTipica(array):
    desviacionTipica=varianza(array)**(0.5)
    return desviacionTipica

diccionario={}

def datos(array):
    a=media(array)
    b=varianza(array)
    c=desviacionTipica(array)
    diccionario.update({"media":a,"varianza":b,"desviacion tipica":c})
    return diccionario

lista=[1,2,3,4]
print(datos(lista))        #prueba

#2. Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
def mcm(a,b):
    i=1
    while True:
        if (i%a==0 and i%b==0):
            return i
        i += 1

def mcd(a,b):
    if(a<b):
        c=a
    else:
        c=b
    while True:
        if (a%c==0 and b%c==0):
            return c
        c -= 1

print(mcm(2,4))     #prueba
print(mcd(2,4))

#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
texto=["Cadena ", " de ", "caracteres", " de ", "prueba"]
diccionario={}
for palabra in texto:
    veces= texto.count(palabra)
    diccionario.update({palabra:veces})
print(diccionario)

# #Ejercicios listas y tuplas

#1. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
asignaturas=["Matematicas", "Fisica", "Quimica", "Historia"]
for materia in asignaturas:
    print("Yo estudio: " + materia)
    
#2. Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
ganador=input("Ingrese los 6 numeros ganadores con un espacio de por medio: ")
list=ganador.split()
list.sort
print(list)

#3. Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
precios=[50, 75, 46, 22, 80, 65, 8]
menor=None
mayor=None
for numero in precios:
    if menor==None and mayor==None:
        mayor=numero
        menor=numero
    else:
        if numero<menor:
            menor=numero
        if numero>mayor:
            mayor=numero
print("El mayor es:", mayor)
print("El menor es: ", menor)
# #Ejercicio diccionarios

#1. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
direccion=input("Ingrese su direccion: ")
tel=int(input("Ingrese su telefono: "))

dic= {"nombre":nombre,"edad":edad,"direccion":direccion,"telefono":tel}
print(dic["nombre"]," tiene ", dic["edad"]," años, vive en ", dic["direccion"],"y su número de teléfono es",dic["telefono"])

#2. Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
dicc={}

nombre=input("Ingrese su nombre: ")
dicc.update({"Nombre: ":nombre})
print(dicc)

edad=int(input("Ingrese su edad: "))
dicc.update({"Edad: ":edad})
print(dicc)

sexo=input("Ingrese su sexo biologico: ")
dicc.update({"Sexo: ":sexo})
print(dicc)

tel=int(input("Ingrese su telefono: "))
dicc.update({"Telefono: ":tel})
print(dicc)

