#*Ejercicios Condicionales*

#1.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene 
# entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.


#Ejercicios Bucles

#1.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
# el número de veces que aparece la letra en la frase



# edad = int (input ("Escriba su edad: "))
# edadMayor = 18
# edadMenor = 4

# if edad < edadMenor:
#     print ("Estra gratis")

# elif edad <= edadMayor:
#     print("Debe pagar 5€")

# else:
#     print("Debe pagar 10€")




frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))