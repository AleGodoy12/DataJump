#1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad=int(input("Ingrese su edad: "))
cumple=0
while(cumple<edad):
    cumple+=1
    print("Cumplió: ", cumple, " años")

# 2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas
num=int(input("Ingrese un numero entero positivo: "))
regresiva=num
while(regresiva>0):
    print(regresiva, end = ", ")
    regresiva-=1
                                        

# 3.- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
dinero=float(input("Ingrese el monto a invertir: "))
interes=float(input("Ingrese el porcentaje de interes anual: "))
años=int(input("Ingrese la cantidad de años: "))
i=1
while(i<=años):
    capital=dinero*(interes/100)*i+dinero
    print("El capital del ", i, " año es de :", capital)
    i+=1

# 4.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
numero=int(input("Ingrese un numero entero: "))

contador=0

for i in range(2,numero):
    resto=numero%i
    if (resto==0):
        contador +=1
if (contador>=1):
    print("No es primo")
else:
    print("Es primo")

# 5.- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra=input("Ingrese una palabra: ")
largo=len(palabra)

for letra in range(len(palabra)-1,-1,-1):         
        print(palabra[letra])                                    

# 6.- Escribir un programa que muestre todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
texto=input("Escriba lo que quiera (para dejar de mostrar escriba salir): ")
while(texto != "salir"):
    texto=input("Escriba lo que quiera (para dejar de mostrar escriba salir): ")
print("Usted ha salido")

# 7.- Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función
pi=3.14
def area(radio):
    y=pi*(radio**2)
    return y

r=float(input("Ingrese el radio de su circulo: "))
area1=area(r)

print("El area del circulo es: ", area1, " cm²")


h=float(input("Ingrese la altura de su cilindro: "))
volumen=area1*h

print("El volumen de su cilindo es: ", volumen, "cm³")

# 8.- Escribir una función que reciba un número entero positivo y devuelva su factorial
def factorial(numero):
    if (numero==0):
        return 1
    else:
        return numero * factorial(numero - 1)
        
number=int(input("Ingrese un numero entero positivo: "))
factorial(number)           #no me devuelve el factorial pero el codigo esta bien


# 9.- Escribir una función que reciba una muestra de números en una lista y devuelva su media.
def media(array):
    cant=len(array)
    suma=0
    for i in array:
        suma+=i
    media=cant/suma
    return media
        

# 10.- Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def saludar():
    saludo="Hola amiga!"
    return saludo
    
print(saludar())

