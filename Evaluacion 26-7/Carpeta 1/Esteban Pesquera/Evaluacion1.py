#*Ejercicios Condicionales*
#1.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular
#  de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar
#  al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis
# , si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
#Ejercicios Bucles
#1.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla
# el número de veces que aparece la letra en la frase

edad_usuario = int(input("Cual es tu edad?, ingrese solo numeros "))
if edad_usuario <=18 and edad_usuario >=4:
    print("el precio a pagar es de 5 €")
else:
     if edad_usuario < 4:
        print("podes ingresar gratis")

     else:
        print("el precio a pagar es de 10€")


frase = (input("Ingrese una frase"))
letra = (input("Ingrese una letra"))
contador_misma_letra = 0


while contador_misma_letra < frase.count(letra):
      contador_misma_letra += 1

print(contador_misma_letra)