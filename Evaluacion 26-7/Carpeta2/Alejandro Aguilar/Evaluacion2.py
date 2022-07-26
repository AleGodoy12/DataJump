#*Ejercicios Condicionales*

#1.-Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
# por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la 
# guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseña = "asd12345"
ingreso = input ("Introduzca su contraseña").lower()
if (contraseña == ingreso):
    print(" Bienvenido..")
else:
    print("Datos inválidos, vuelva a intentar")


#Ejercicios Bucles

#1.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
# el número de veces que aparece la letra en la frase

frase = input("Frase: ")
letraBuscada = input("Letra: ")
contador = 0
for letra in frase:
    if(letra == letraBuscada):
        contador += 1
print("Cantidad de veces que aparece la letra '" + letraBuscada + "' en la frase '" + frase + "': " + str(contador))

#10/10