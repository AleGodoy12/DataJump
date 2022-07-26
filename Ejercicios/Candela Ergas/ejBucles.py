# *Ejercicios Bucles*

# 1.- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra= str(input("Escribí una palabra: "))
print((palabra+" ")*10)

# 2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares 
# desde 1 hasta ese número separados por comas.

num=int(input("Ingresa un numero entero: "))
i=1
if (type(num)==int) and num>1:
    print("Los números impares hasta ",num," son:")
    while i<=num:
        if (i%2 != 0):
            print(i)
        i+=1
# else:
#     print("El valor ingresado:'"+num+ "' es incorrecto")

# 3.- Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10

numA=1

while numA<=10:
    print("Tabla del:",numA)
    for num in range(1,11):  
        total=numA*num
        print(numA,"*",num,"=",total)
    numA+=1


# 4.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña 
# hasta que introduzca la contraseña correcta.

clave="clave1234"
contraseña= str(input("Ingresá la contraseña: "))

while (clave!=contraseña):
        print("Contraseña incorrecta, intentá de nuevo")
        contraseña= contraseña=str(input("Ingresá la contraseña: "))

if (clave==contraseña):
        print("Contraseña correcta!")

# 5.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que
#  aparece la letra en la frase
frase=str(input("Ingresá una frase: "))
letra=str(input("ingresá una letra: "))

print("La letra '",letra,"' aparecece ", frase.count(letra)," veces en la frase ingresada")