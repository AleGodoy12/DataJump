# 1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
# edad = int(input("Ingrese su edad: "))

# if (edad >= 18):
#     print("Usted es mayor de edad!")
# else: 
#     print("Usted es menor de edad!")

# 2.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
# CONTRASEÑA = "boquitapapa"
# contraseñaIngre = input("Ingrese su contraseña: ").lower()

# if(CONTRASEÑA == contraseñaIngre):
#     print("La contraseña coincide, puede continuar...")
# else:
#     print("La contraseña no coincide, vuelva a intentar!")

# 3.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
# num = int(input("Ingrese un número, plis: "))

# if( num%2 == 0 ):
#     print(f"El número {num} es par")
# else:
#     print(f"El número {num} es impar")

# 4.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
# entradaEdad = int(input("Ingrese su edad: "))

# if(entradaEdad >= 1 and entradaEdad < 4):
#     print("Puede ingresar gratis")
# elif(entradaEdad >= 4 and entradaEdad < 18):
#     print("Debe pagar 5€")
# elif(entradaEdad >= 18):
#     print("Debe pagar 10€")

# 5.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
ABECEDARIO = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

primeraParte = ABECEDARIO[:13]
segundaParte = ABECEDARIO[13:27]

grupoA = []
grupoB = []

i = 0
a = 0

sexo = input("Ingrese su sexo: (masculino / femenino) -> ").lower()
nombre = input("Ingrese tu nombre: ").lower()
primerLetra = nombre[0]

validacion = primerLetra in primeraParte
validacion2 = primerLetra in segundaParte
print(validacion)

if (sexo == "femenino" and validacion or sexo == "masculino" and validacion2):
    grupoA.append(nombre)
else:
    grupoB.append(nombre)

print(f"En el grupo A están: {grupoA} y en el grupo B están: {grupoB}")

# if(sexo == "masculino" and validacion2):
#     grupoA.append(nombre)
# else:
#     grupoB.append(nombre)

# if(sexo == "femenino"):
#     while(i < len(primeraParte)):
#         if(primeraParte[i] == primerLetra):
#             grupoA.append(nombre)
#     i += 1
#     grupoB.append(nombre)

# elif(sexo == "masculino"):
#     while(a < len(segundaParte)):
#         if(segundaParte[a] == primerLetra):
#             grupoA.append(nombre)
#         a += 1
#     grupoB.append(nombre)
# else:
#     print("sexo mal escrito!")

#El grupo A estan: ['zamuel'] y en el grupo B estan: ['zamuel'] sale eso al seleccionar masculino, zamuel
#falta corregir