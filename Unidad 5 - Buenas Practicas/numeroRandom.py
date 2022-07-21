from random import *                                                      #Importamos el modulo random
def generaNumeroAleatorio(minimo, maximo):         #definimos una funcion propia
    return randint(minimo, maximo)                #retornamos un numero aleatorio


numero_buscado=generaNumeroAleatorio(1,100)       #Llamamos a la funcion propia
encontrado=False                                                           
intentos=0


while not encontrado:                                    #Bucle a repetir mientras negado sea falso
    while True:                                                               #Comenzamos el manejo de excepcion
        try:           
            numero_usuario=int(input("Introduce el numero buscado:  "))
            break
        except ValueError:                                                       #En caso de error de tipo de dato
            print("El valor ingresado debe ser un numero, por favor reintente.")
    if numero_usuario>numero_buscado:                 #compara el valor random y del usuario
        print("El numero que buscas es menor")             #Si el de usuario es mayor se ejecuta
                                                                                           # este bloque
        intentos=intentos+1
    elif numero_usuario<numero_buscado:                #Este otro si el del usuario es menor
        print("El numero que buscas es mayor")
        intentos=intentos+1
    else:                                                    #Cuando el usuario acierta, se ejecuta este bloque.
        encontrado=True                  #Se cambia el valor del booleano para terminar el bucle.
print("Has acertado, el numero correcto es ", numero_usuario, "te ha llevado", intentos, "intentos")