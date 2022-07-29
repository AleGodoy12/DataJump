#1

edad = int(input('Ingresá tu edad'))
año = 2022
i = (2022 - edad)
while (i < año):
    i+=1
    print(i)

#2 
num = int(input('Ingresá número entero positivo'))
i=num
while (i<=num and i>0):
    i-=1
    print (i)

#3
inversion = int(input('Decime la cantidad que querés invertir'))
intAnual = float(input('El interés anual'))
años = int(input('Años que invertirás'))
i = 1
while (i<=años):
    total = inversion * (intAnual/100) * i + inversion
    print (total)
    i += 1 

#4
num = int(input('Ingresá un número entero'))
if num > 1:
    for i in range(1, num):
        if (num == 2):
            print('Es un n°primo')
        elif (num % i) == 0:
            print('No es un n° primo')
            break
        else:
            print('Es un n° primo')
    
#5
palabra = input('Decime una palabra')
for i in reversed(palabra):
    print(i)

#6 
algo = input('Introducí algo')
while (algo != 'salir'):
    print(algo)
    algo = input('Introducí algo')


#7
radio = float(input('Introduci un radio'))

def area (uwu):
    radio = 3.14 * uwu ** 2
    return radio

print(area(50))


def volumen (altura, radio):
    volCilindro = 3.14 * altura * (radio ** 2)
    return volCilindro

print(volumen(50, 10))

#8
def fact (num):
    i = 0
    acc = 1
    while (i < num):
        i += 1
        acc *= i
    print(acc) 
fact(5)

#9
def media (array):
    prom= sum(array) / len(array)
    return prom
media([10, 20, 30, 40, 50])    

#10 
def saludo():
    print('¡Hola amiga!')
saludo()