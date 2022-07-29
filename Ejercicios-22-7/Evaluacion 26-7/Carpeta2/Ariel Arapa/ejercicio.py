#*Ejercicios Condicionales*

#1.-Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la 
# guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
contraseña = "contraseña"
contraIngre = input("Ingrse su contraseña: ").lower()

if(contraseña == contraIngre):
    print("Contraseña correcta!")
else:
    print("Contraseña invalida!")

#Ejercicios Bucles

#1.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
# el número de veces que aparece la letra en la frase

frase = input("Ingrese una frase: ").lower()
letra = input("Ingrese una letra: ").lower()
x = 0
contador = 0
while (x < len(frase)):
    if(frase[x] == letra):
        contador += 1
    x += 1

print(f"La letra {letra.upper()} se repite {contador} veces.")

#10/10