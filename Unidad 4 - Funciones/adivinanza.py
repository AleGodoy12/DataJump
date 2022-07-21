from random import *
def generaNumeroAleatorio(minimo, maximo):
return randint(minimo, maximo)
numero_buscado=generaNumeroAleatorio(1,100)
encontrado=False
intentos=0
while not encontrado:
    numero_usuario=int(input("Introduce el numero buscado: "))
    if numero_usuario>numero_buscado:
        print("El numero que buscas es menor")
        intentos=intentos+1
    elif numero_usuario<numero_buscado:
        print("El numero que buscas es mayor")
        intentos=intentos+1
    else:
        encontrado=True
        print("Has acertado, el numero correcto es ", numero_usuario, "te ha llevado", intentos, "intentos")