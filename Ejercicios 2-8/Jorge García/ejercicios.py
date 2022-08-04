import math

#1 Escribir una función que reciba una muestra de números en una lista y 
# devuelva un diccionario con su media, varianza y desviación típica.

def calcularEstadisticas(datos):
    estadisticas = {}
    media = sum(datos)/len(datos)
    sumaDesvios = 0
    for i in datos:
        desvio = pow(i - media, 2)
        sumaDesvios += desvio
    varianza = sumaDesvios/len(datos)
    desvio = math.sqrt(varianza)
    estadisticas["Media"] = media
    estadisticas["Varianza"] = varianza
    estadisticas["Desvio"] = desvio
    return estadisticas

lista = [48, 48, 51, 52, 55, 56, 57, 58, 60, 61]
print(calcularEstadisticas(lista))

#2 Escribir una función que calcule el máximo común divisor de dos números 
# y otra que calcule el mínimo común múltiplo.

def calcularMCD(num1, num2):
    if(num1 == num2):
        return num1
    numMayor = max(num1, num2)
    numMenor = min(num1, num2)
    resto = numMayor % numMenor
    if(resto == 0):
        return numMenor
    else:
        dividendo = numMenor
        divisor = resto
        resto = dividendo % divisor
        while resto != 0:
            dividendo = divisor
            divisor = resto
            resto = dividendo % divisor
        return divisor

def calcularMCM(num1, num2):
    resultado = num1*num2/calcularMCD(num1, num2)
    return resultado

resultado = calcularMCD(24, 75)
print("MCD =", resultado)

resultado = calcularMCM(180, 67)
print("MCM =", resultado)

#3 Escribir un programa que reciba una cadena de caracteres y 
# devuelva un diccionario con cada palabra que contiene y su frecuencia. 
# Escribir otra función que reciba el diccionario generado con la función anterior 
# y devuelva una tupla con la palabra más repetida y su frecuencia.

def calcularOcurrencias(texto):
    texto = texto.lower()
    ocurrencias = {}
    lista = texto.split(' ')
    for letra in lista:
        ocurrencias[letra] = ocurrencias.get(letra, 0) + 1
    return ocurrencias

def guardarOcurrencias(dic_ocurrencias):
    max = 0
    palabra_max = ""
    for clave, valor in dic_ocurrencias.items():
        if(valor > max):
            max = valor
            palabra_max = clave
    return (palabra_max, max)


texto = "hola hola como como como como como estas estas estas"
dic_occurrencias = calcularOcurrencias(texto)
print(dic_occurrencias)
tupla_ocurrencias = guardarOcurrencias(dic_occurrencias)
print(f"Palabra que más se repite: {tupla_ocurrencias}")

#4 Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
# donde <asignatura> es cada una de las asignaturas de la lista.

materias = ["Matemáticas", "Física", "Historia", "Química", "Lengua"]
for asignatura in materias:
    print(f"Yo estudio {asignatura}.")

#5 Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

numerosGanadores = []
for i in range(5):
    numero = int(input("Ingresa un número ganador: "))
    numerosGanadores.append(numero)
numerosGanadores.sort()
print(numerosGanadores)

#6 Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8
# y muestre por pantalla el menor y el mayor de los precios.

precios = [50, 75, 46, 22, 80, 65, 8]
menorPrecio = min(precios)
maxPrecio = max(precios)

print(f"Menor precio: {menorPrecio}")
print(f"Mayor precio: {maxPrecio}")

#7 Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono 
# y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
# vive en <dirección> y su número de teléfono es <teléfono>.

nombre = input("Nombre: ").capitalize()
edad = int(input("Edad: "))
direccion = input("Dirección: ").capitalize()
telefono = input("Teléfono: ")

if(edad > 0 and edad < 100 and nombre.isalpha()):
    persona = {}
    persona['Nombre'] = nombre 
    persona['Edad'] = edad 
    persona['Direccion'] = direccion 
    persona['Telefono'] = telefono 
    print(f"{persona['Nombre']} tiene {persona['Edad']} años, vive en {persona['Direccion']} y su número de teléfono es {persona['Telefono']}")
else:
    print("Datos inválidos.")

#8 Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una datos 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

datos = {}

nombre = input("Nombre: ").capitalize()
datos['Nombre'] = nombre
print(datos)
edad = int(input("Edad: "))
datos['Edad'] = edad 
print(datos)
sexo = input("Sexo: ")
datos['Sexo'] = sexo 
print(datos)
direccion = input("Dirección: ").capitalize()
datos['Direccion'] = direccion 
print(datos)
telefono = input("Teléfono: ")
datos['Telefono'] = telefono 
print(datos)
mail = input("Correo electrónico: ")
datos['Mail'] = mail 
print(datos)
