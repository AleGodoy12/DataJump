#BUCLES

#1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Ingrese su edad: "))   

if(edad > 18):
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")
    
#2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numeroEntero = int(input("Ingrese un número entero que sea positivo: "))
impares = []

if(numeroEntero > 0):
    for impar in range(1, numeroEntero+1):
        if(impar % 2 != 0):
            impares.append(impar) #agrega los impares como el ultimo elemento al array
    print(impares)
else:
    print("Número inválido")

#3.- Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10

multiplicando = int(input("Quiero la tabla del: "))

multiplicador = 0

while (multiplicador < 10):
    multiplicador += 1
    resultado = multiplicando * multiplicador
    print(multiplicando, "X", multiplicador, "=", resultado)

#4.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña = "estaeslacontraseña"
contraseñaIngresada = ""

while contraseña != contraseñaIngresada:
    contraseñaIngresada = input("Ingrese la contraseña: ")
print("Contraseña correcta")


#5.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase

frase = input("Escriba una frase: ")
letraIngresada = input("Escriba la letra que quiere buscar: ")
contador = 0
for letra in frase:
    if letra == letraIngresada:
        contador +=1

print("La cantidad de veces que aparece la letra " + letraIngresada + " en la frase " + frase + ": " + str(contador))