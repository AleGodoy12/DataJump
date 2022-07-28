#*Ejercicios Condicionales*

#1.-Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la 
# guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password=str(input("Ingrese la contraseña: ")).lower()
contraseña="arbusta123"
if(password==contraseña):
    print("Contraseña correcta!")
else:
    print("Lo siento, contraseña incorrecta")

#Ejercicios Bucles

#1.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
# el número de veces que aparece la letra en la frase

frase=str(input("Ingrese una frase: ")).lower()
letra=str(input("Ingrese una frase: ")).lower()

cant=0

for i in frase:
    if(i==letra):
        cant+=1
print("La letra ", letra, "aparece ", cant, " veces")



#10/10