
#*Ejercicios Condicionales*

#1.-Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña
# e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseña="eval-26/7"
contUser=(input("Ingresá la contraseña: "))

if contraseña.lower() == contUser.lower():
    print("Contraseña correcta")
else:
    print("contraseña incorrecta")

#Ejercicios Bucles

#1.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
# el número de veces que aparece la letra en la frase
frase=(input("Ingresá una frase:"))
letra=(input("Elegi una letra:"))
cant= (frase).count(letra)

print("La letra '",letra,"' aparece ",cant,"veces en la frase ingresada")

#10/10