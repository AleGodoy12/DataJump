# Ejercicios Bucles

# 1.- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = str (input("Introduzca una palabra: "))
for i in range(10):
    print(palabra)
# 2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números
#     impares desde 1 hasta ese número separados por comas.
numero = int (input("Inserte un número: "))
contadorImpares = []
for i in range (1, numero, 1):
  if i % 2 != 0:
    contadorImpares.append(i)
print (contadorImpares)

# 3.- Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10

numero = int (input("Ingrese un número: "))
for i in range (1, 11):
    
    multiplicacion = i * numero 
    
    print("La multiplicaión de ", numero, " * ", i, " = ", multiplicacion)
    
# 4.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
#     por la contraseña hasta que introduzca la contraseña correcta.

passwordC = str (input("Ingrese su contraseña: "))
passwordcorrect = "arusta744"
while (passwordC != passwordcorrect):
    print ("contraseña erronea ")
    passwordC = str (input("Introduzca su contraseña: "))
if (passwordC == passwordcorrect):
    print("Contraseña correcta")
    
# 5.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el
#     número de veces que aparece la letra en la frase


frase = input("Ingrese una frase: ").lower()
letra = input("Ingrese una letra: ").lower()
contador, i = 0, 0

while(i < len(frase)):
    if(frase[i] == letra):
        contador += 1
    i += 1

print(f"La letra {letra} aparece {contador} veces en la frase ingresada.")