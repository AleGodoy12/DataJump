#FUNCIONES
#1 
dicc = {}
array = [10,15,25]
def media (array):
    prom = sum(array)/len(array)
    return prom

def var (array):
    calculo = 0 
    for i in array:
        calculo += ((i - media(array)) **2)
    varianza = (calculo / len(array))
    return varianza

def desviacionT (array):
    des = var(array)**0.5 
    return des

dicc['Media'] = media(array)
dicc['Varianza'] = var(array)
dicc['Desviación Típica'] = desviacionT(array)
print(dicc)

#2 
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
#4
materias = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
for i in materias:
    print('Yo estudio', i, 'en la posición' , materias.index(i))

# 5 
numGanadores = int(input('Decime los 6 números ganadores de la lotería'))
numSeparados = numGanadores.split()
numSeparados.sort()
print(numSeparados)

#6 
precios = [ 50, 75, 46, 22, 80, 65, 8]
print(min(precios), max(precios))

#EJERCICIOS DICCIONARIOS
#7
dicc = {}
nombre = input('Ingresá tu nombre')
edad = input('Ingresá tu edad')
direccion = input('Ingresá tu dirección')
telefono = input('Ingresá tu teléfono')

dicc['Nombre'] = nombre
dicc['Edad'] = edad
dicc['Dirección'] = direccion
dicc['Telefono'] = telefono
print(dicc)

#8

dicc = {}
i = 1
info = '?'
dato = '?'

while (i != 0):
    info = input('Información a ingresar')
    dato = input('El dato respectivo de la información agregada')
    dicc[info]=dato
    print(dicc)
