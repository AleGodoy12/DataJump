# #Ejercicios funciones

# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.


# import math
# from statistics import stdev, variance


# listita= [11, 5, 8, 23, 6, 12, 24]

# media = sum(listita)/len(listita)
# varianza = variance(listita)
# desviacion = stdev(listita)

# def funcionLista(a, b, c):
#     total = a, b, c
#     return total
# print(funcionLista(media, varianza, desviacion))

    
# # Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

# import math  

# # a = int(input("Ingrese un numero: "))
# # b = int(input("Ingrese otro numero:"))


# def dcm(a, b):
#     return math.gcd(a, b)
# print(dcm(60, 30))
# def mcm(a, b):
#     return (a * b) / dcm(a, b)

# print(mcm(60, 30))
# print(mcm(4, 10))


# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

programa = ["Hola", "como estas?", "ya comiste?"]
programa2 = ["Hola", "bien", "sí" ]

dicio = {}

for key in programa:
    for value in programa2:
        dicio[key]= value
    break
print(dicio)


# #Ejercicios listas y tuplas

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

# materias = ("Matemáticas", "Física", "Química", "Historia" , "Lengua")

# for a in materias:
#     print(f"Yo estudio {a} dónde {a} es cada una de las asignaturas de la lista.")

# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# ganadores = []

# for g in range(5):
#     ganadores.append(int(input("Ingrese los números ganadores: ")))
# ganadores.sort()
# print("Los numeros ganadores de la loto son ", ganadores)


# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

# precios= [ 50, 75, 46, 22, 80, 65, 8]
# min = max = precios[0]
# for p in precios:
#     if p < min:
#         min = p
#     if p > max:
#         max = p
# print(f"El minimo es {min} y el maximo es {max}")

# # #Ejercicio diccionarios

# # Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
# nombre = str(input("Ingrese su nombre: "))
# edad = int(input("Ingrese su edad: "))
# dirrecion = str(input("Ingrese su domicilio: "))
# telefono = int(input("Ingrese su numero de telefono: "))

# diccionario = { "Nombre": nombre, "Edad": edad, "Direccion": dirrecion, "Numero telefonico": telefono
# }

# print(diccionario ["Nombre"], "tiene", [edad], "años", "vive en", [dirrecion], "y su numero de telefono es ", [telefono])



# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.



    
