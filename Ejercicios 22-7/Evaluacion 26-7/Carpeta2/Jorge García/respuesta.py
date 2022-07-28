#*Ejercicios Condicionales*

#1.-Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la 
# guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

clave = "evaluacion123"
clave = clave.lower()
claveIngresada = input("Ingresa la contraseña: ")
if(clave == claveIngresada.lower()):
    print("¡Clave correcta!")
else:
    print("Clave incorrecta. Inténtalo de nuevo más tarde.")

#Ejercicios Bucles

#1.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
# el número de veces que aparece la letra en la frase

frase = input("Ingresa una frase: ")
letraBuscada = input("Ingresa una letra: ")
contador = 0
for letra in frase:
    if(letra == letraBuscada):
        contador += 1
print("Cantidad de veces que aparece la letra '" + letraBuscada + "' en la frase '" + frase + "': " + str(contador))