#*Ejercicios Condicionales*

#1.-Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la 
# guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


contraseña= "holamundo123"
contraseñaIngresada= input("Ingrese una contraseña: ").lower()

if( contraseña == contraseñaIngresada):
    print("Conectado, bienvenidx")
else:
    print("Contraseña incorrecta, intente nuevamente")
    


#Ejercicios Bucles

#1.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
# el número de veces que aparece la letra en la frase

frase = input("Escriba una frase: ")

letraBuscada = input("Escriba la letra que quiere buscar: ").lower()

aparece = 0

for letra in frase:
    if(letraBuscada == letra):
        aparece += 1

print("La letra", letraBuscada , "aparece", aparece, " veces en la frase", frase)