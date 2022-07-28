# 1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
def años():
    edad=int(input("Cuantos años tenés? "))
    año=1
    print("Desde que naciste cumpliste: ", end="")
    while año< edad:
        print (año, end=", ")
        año+=1
    print (edad)
años()

# 2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas

def ej2():
    num=int(input("Insertá un número positivo: "))
    i=num 
    if num>0:
        while i>0 :
            print(i, end=",")
            i-=1
        print(i)
    else:
        print("Es negativo")
ej2()


# 3.- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

def inversion():
    inv=int(input("Ingresá cuánto querés invertir: "))
    interes=int(input("Ingresá el interes anual: "))
    años=int(input("Ingresá por cuantos años: "))

    año=1

    while año<= años:
        interesTotal= interes*año    
        capital=inv+ (inv*interesTotal)/100
        print("El capital obtenido en el año ",año," es de : $",capital)
        año+=1
inversion()


# 4.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

def nPrimos():
    num=int(input("Ingresá un numero entero: "))
    resto=0

    for i in range(2,num): 
        if (num%i==0):
            resto +=1
    if (resto==0):
        print("Es primo")
    else:
        print("No es primo")  
nPrimos()  


# 5.- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def deletrear():
    palabra=(input("Introduci una palabra: "))
    for letra in reversed(palabra):
        print(letra)
deletrear()


# 6.- Escribir un programa que muestre todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
def pClave():
    palabra=str(input("introduci una palabra "))
    clave="salir"
    while palabra!=clave:
            palabra=str(input("introduci una palabra: "))
pClave()


# 7.- Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función

def calcular(radio):
    area= 3.14*(radio**2)
    return (area)
r=float(input("Ingresá el radio del objeto: "))
areaA=calcular(r)
print("El area es ",areaA,"cm²")

altura=float(input("Ingrese la altura de su cilindro: "))
cilindro=areaA*altura

print("El volumen de su cilindro es ", cilindro, "cm³")


# 8.- Escribir una función que reciba un número entero positivo y devuelva su factorial

def factorial():
    num= int(input("Ingresá un número positivo: "))
    i=0
    acum=1
    if num>0:
        while i<num:
            i+=1
            acum= acum*i
        print("El factorial de ",num," es: ",acum)
    else: 
        print("Error!El número debe ser positivo")

factorial()


# 9.- Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def media(array):
    promedio= sum(array)/len(array)
    return promedio

print(media([10,20,30,40]))


# 10.- Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def saludo():
    print("¡Hola amiga!")

saludo()