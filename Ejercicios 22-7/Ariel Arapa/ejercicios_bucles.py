# 1.- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
# palabra = input("Ingrese una palabra: ")
# i = 0
# while(i < 10):
#     print(palabra)
#     i += 1

# 2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
# number = int(input("Ingrese un número: "))
# i = 0
# impares = []
# while (i <= number):
#     if(i%2 == 1):
#         impares.append(i)
#     i += 1

# print(impares)

# 3.- Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
# a, i = 1, 1

# while(i <= 10):
#     print(f"Tabla del {i} de multiplicar: ")
#     a = 1 #restablezco a 1 la variable a para que se vuelva ejecutar el while.
#     while(a <= 10):
#         print(f"{i} x {a} = {i*a}")
#         a += 1
#     i += 1


# 4.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
# CONTRASEÑA = "Eldueño01"
# validar = True

# while(validar):
#     contra = input("Ingrese su contraseña: ")
#     if(contra == CONTRASEÑA):
#         print("Contraseña correcta, puede seguir...")
#         validar = False
#     else:
#         print("Contraseña incorrecta, vuelva a intentar!")

# 5.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase
frase = input("Ingrese una frase: ").lower()
letra = input("Ingrese una letra: ").lower()
contador, i = 0, 0

while(i < len(frase)):
    if(frase[i] == letra):
        contador += 1
    i += 1

print(f"La letra {letra} aparece {contador} veces en la frase ingresada.")