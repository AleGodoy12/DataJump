import math

# Escribir una función que reciba una muestra de números en una lista y 
# devuelva un diccionario con su media, varianza y desviación típica.

def calcularEstadisticas(datos):
    estadisticas = {}
    media = sum(datos)/len(datos)
    sumaDesvios = 0
    for i in datos:
        desvio = pow(i - media, 2)
        sumaDesvios += desvio
    varianza = sumaDesvios/len(datos)
    desvio = math.sqrt(varianza) #math.sqrt calcula la raiz cuadrada del número pasado por parámetro
    estadisticas["Media"] = media
    estadisticas["Varianza"] = varianza
    estadisticas["Desvio"] = desvio
    return estadisticas

lista = [48, 48, 51, 52, 55, 56, 57, 58, 60, 61]
print(calcularEstadisticas(lista))

# Escribir una función que calcule el máximo común divisor de dos números 
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
        # Algoritmo de Euclides: Si la división no es exacta el resto 
        # pasa a ser el divisor de la división siguiente
        # y el divisor actual pasa a ser el dividendo de la división siguiente.
        # Asi hasta que el resto sea igual a 0.
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

# Escribir un programa que reciba una cadena de caracteres y 
# devuelva un diccionario con cada palabra que contiene y su frecuencia. 
# Escribir otra función que reciba el diccionario generado con la función anterior 
# y devuelva una tupla con la palabra más repetida y su frecuencia.

def calcularOcurrencias(texto):
    texto = texto.lower()
    ocurrencias = {}
    lista = texto.split(' ')
    for palabra in lista:
        ocurrencias[palabra] = ocurrencias.get(palabra, 0) + 1
    return ocurrencias

def obtenerPalabraFrecuente(dic_ocurrencias):
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
tupla_ocurrencias = obtenerPalabraFrecuente(dic_occurrencias)
print(f"Palabra que más se repite: {tupla_ocurrencias}")

# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
# donde <asignatura> es cada una de las asignaturas de la lista.

materias = ["Matemáticas", "Física", "Historia", "Química", "Lengua"]
for asignatura in materias:
    print(f"Yo estudio {asignatura}.")

# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

numerosGanadores = []
intentos = 6

while intentos > 0:
    numero = int(input("Ingresa un número ganador entre 1 y 49: "))
    if(numero in numerosGanadores):
        print(f"El número {numero} ya estaba, ingresa otro.")
        continue
    if(numero > 0 and numero < 50):
        numerosGanadores.append(numero)
        intentos -= 1
    else:
        print("Número inválido, debes ingresar un número entre 1 y 49")
        
numerosGanadores.sort()
print(f'Números ganadores: {numerosGanadores}')

#6 Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8
# y muestre por pantalla el menor y el mayor de los precios.

precios = [50, 75, 46, 22, 80, 65, 8]
menorPrecio = min(precios)
maxPrecio = max(precios)

print(f"Menor precio: {menorPrecio}")
print(f"Mayor precio: {maxPrecio}")

# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono 
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

# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una datos 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

respuesta = 0
persona = {}
while respuesta != 1:
    dato = input("Ingresa el dato que quieres agregar: ")
    valor = input(f"Ingresa tu {dato}: ")
    persona[dato] = valor
    print(persona)
    respuesta = int(input("Si quieres salir ingresa [1], si no ingresa [2]: "))