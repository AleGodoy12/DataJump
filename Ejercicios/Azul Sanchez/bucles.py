# 1.- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra= input("Ingrese una palabra: ")     # input: para que ingrese datos
i= 0                                        # i= contador
while(i < 10):                              # hago while para que genere el bucle y me muestre varias veces lo que pido hasta terminarlo.
    print(palabra)
    i +=1                                   # acumulador

# 2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input("Por favor ingrese un número entero positivo: "))

for i in range(1, numero+1, 2):             # for: dato que va a usar de una lista
    print(i, end=", ")                      # in: hace referencia donde va a buscar los datos
                                            # range: rango 
                                            #(2): para que vaya de 2 y muestre los impares 1,3,5

# 3.- Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10

número= int(input("Ingrese un número del 1 al 10: "))
multiplicador= 0
while (multiplicador<10):
    multiplicador += 1
    resultado= número * multiplicador
    print(número, "x", multiplicador, "=", resultado)

# 4.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

clave= "Hola123"
contraseña= input("¿Cuál es su contraseña? ").capitalize()   # deja la mayuscula como esta
if(clave == contraseña):
    print("Contraseña correcta ")                
else:
    print("Contraseña incorrecta ")  


# 5.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase

frase= input("Ingrese una frase: ")                 
letra= input("Ingrese una letra: ")
contador, i= 0,0                                   

while(i < len(frase)):
    if(frase[i] == letra):
        contador += 1
    i += 1
print(f"La letra", letra, "aparece", contador, "veces en la frase.")