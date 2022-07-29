#*Ejercicios Condicionales*

#1.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene 
# entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.


#Ejercicios Bucles

#1.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
# el número de veces que aparece la letra en la frase

# Ejercicios Condicionales 

edad = int(input("Ingrese su edad"))

if edad < 4:
    print("Entra gratis")
elif edad >= 4 and edad < 18:
    print("Debe pegar 5€")
else:
    print("Debe pagar 10€")

# Ejercicios bucles

frase = str(input("Ingrese una frase")).casefold()
letra = str(input("Ingrese una letra")).casefold()

for coincidencia in frase:
    contador = frase.count(letra)
print(contador)

#10/10