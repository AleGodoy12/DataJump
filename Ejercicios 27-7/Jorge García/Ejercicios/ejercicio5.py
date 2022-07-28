# 5.- Escribir un programa que pida al usuario una palabra y 
# luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = input("Ingresa una palabra: ")
indice = len(palabra)-1
while indice >= 0:
    print(palabra[indice])
    indice -= 1