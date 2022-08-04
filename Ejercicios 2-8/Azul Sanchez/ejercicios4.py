#1. Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
dicc= {}
                                         #REVISAR 
def calculos (lista):
    media= sum(lista)/len(lista)
 
#2. Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

num1=200
num2=150                                 #REVISAR MCM

def mcd(a, b):
    resto = 0
    while(b > 0):
        

    

def mcm(a, b):
    return(a * b) / mcd
mcm2= mcm (num1, num2)
print("El máximo común divisor de ", num1," y ", num2," es ", mcd(num1, num2))
print("El mínimo común múltiplo de ", num1, "y", num2, "es", mcm2)




#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

#Ejercicios listas y tuplas

#4. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio , donde es cada una de las asignaturas de la lista.

asignaturas= ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
tupla= []

for i in range(len(asignaturas)):
    print("Yo estudio", asignaturas[i])


#5. Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

ganadores= input("Ingrese 6 números ganadores de la lotería primitiva")
lista= []
for i in ganadores:
    lista= sorted(ganadores)
print(lista)

#6. Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios= [50, 75, 46, 22, 80, 65, 8]
min= max= precios [0]

for precio in precios:
    if precio < min:
        min = precio
    elif precio > max:
        max= precio
print("El menor de los precios es: ", min)
print("El mayor de los precios es: ", max)


#Ejercicio diccionarios

#7. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje tiene años, vive en <dirección> y su número de teléfono es <teléfono>.

Nombre= str(input("Ingrese su nombre: "))
Edad= int(input("Ingrese su edad: "))
Dirección= str(input("Ingrese su dirección: "))
Teléfono= int(input("Ingrese su número telefónico: "))

dicc= {"nombre": Nombre, "edad": Edad, "dirección": Dirección, "teléfono": Teléfono}

print(dicc["nombre"], "tiene", dicc["edad"], "años", "vive en", dicc["dirección"], "y su número de teléfono es:", dicc["teléfono"])


#8. Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

dicc= {}
seguir= True
información= input("Ingrese datos personales: ")
