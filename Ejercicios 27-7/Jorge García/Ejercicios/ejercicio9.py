# 9.- Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def calcularMedia(listaNumeros):
    if(len(listaNumeros) > 0):
        acumulador = 0
        for numero in listaNumeros:
            acumulador += numero
        return round(acumulador/len(listaNumeros), 3)
    return 0

lista = [10, 50, 34, 130, 2, 67]
media = calcularMedia(lista)
if(media != 0): 
    print(media)
else:
    print("Lista vacía.")