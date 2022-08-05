 # #Ejercicios funciones

1 # Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

lista=[15,28,35,44]
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

def desviacionTipica(lista):
    desviacionTipica=varianza(lista)**(0.5)
    return desviacionTipica

def varios(lista):
    varios=dict(media=media(lista),varianza=varianza(lista),desvT=desviacionTipica(lista))
    return varios
print(varios(lista))

2 # Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

def maximo_comun_divisor(a, b):

    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

print(maximo_comun_divisor(15, 8))

def mcm (a, b):
    return (a * b) / maximo_comun_divisor(a, b)

print(mcm(15, 8))


3 # Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia.
##Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def Repeticiones(texto):
    texto = texto.lower()
    ocurrencias = {}
    lista = texto.split(' ')
    for palabra in lista:
        ocurrencias[palabra] = ocurrencias.get(palabra, 0) + 1
    return ocurrencias

def PalabraRepetida(dic_ocurrencias):
    max = 0
    palabra_max = ""
    for clave, valor in dic_ocurrencias.items():
        if(valor > max):
            max = valor
            palabra_max = clave
    return (palabra_max, max)


texto = "hi hi chau chau chau probando probando probando probando"
dic_occurrencias = Repeticiones(texto)
print(dic_occurrencias)
tupla_ocurrencias = PalabraRepetida(dic_occurrencias)
print(f"Palabra que más se repite: {tupla_ocurrencias}")

# #Ejercicios listas y tuplas

4 # Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista
# y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

materias = ["Matemáticas", "Física", "Historia", "Química", "Lengua"]
for asignatura in materias:
    print(f"Yo estudio {asignatura}.")

5 # Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
  # los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
  
ganadores= input(" Ingrese los números ganadores ")
lista= []
for i in ganadores:
    lista= sorted(ganadores)
print(lista)

6 # Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y
# el mayor de los precios.

def listado ():
     Precios = [50, 75, 46, 22, 80, 65, 8]

     precioMaximo = max(Precios)
     precioMinimo = min(Precios)

     print(f"El mayor precio es {precioMaximo}")
     print(f"El menor precio es {precioMinimo}")

listado()



 # #Ejercicio diccionarios

7 # Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
##Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

def Usuario ():

    nombre = input(" Introduzca su nombre ")
    edad = int(input(" Introduzca su edad "))
    direccion = input(" Introduzca su dirección ")
    telefono = int(input(" Introduzca su telefono "))

    dic2 = {"Nombre": nombre, "Edad": edad, "Direccion": direccion, "Teléfono": telefono}


    print(dic2["Nombre"], " tiene ", dic2["Edad"], " años, vive en ", dic2["Direccion"], " y su número de teléfono es ", dic2["Teléfono"])

Usuario()


8 # Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
##(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo
# dato debe imprimirse el contenido del diccionario.

informacion = {}

nombre = input("Nombre: ").capitalize()
informacion['Nombre'] = nombre
print(informacion)
edad = int(input("Edad: "))
informacion['Edad'] = edad 
print(informacion)
sexo = input("Sexo: ")
informacion['Sexo'] = sexo 
print(informacion)
direccion = input("Dirección: ").capitalize()
informacion['Direccion'] = direccion 
print(informacion)
telefono = input("Teléfono: ")
informacion['Telefono'] = telefono 
print(informacion)
mail = input("Correo electrónico: ")
informacion['Mail'] = mail 
print(informacion)

