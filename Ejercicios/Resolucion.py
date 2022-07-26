#*Ejercicios Tipo de datos simples:*

#1.- print("¡Hola Mundo!")

#2.- mensaje = "¡Hola Mundo!" 
     #print(mensaje)

#3.- horas = float(input("Introduce tus horas de trabajo: "))
     #coste = float(input("Introduce lo que cobras por hora: "))
     #paga = horas * coste
     #print("Tu paga es", paga)

#4.- peso = input("¿Cuál es tu peso en kg? ")
     #estatura = input("¿Cuál es tu estatura en metros?")
     #imc = round(float(peso)/float(estatura)**2,2)
     #print("Tu índice de masa corporal es " + str(imc))


#5.- barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
    #precio = 3.49 
    #descuento = 0.6
    #coste = barras * precio * (1 - descuento)
    #print("El coste de una barra fresca es " + str(precio) + "€")
    #print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
    #print("El coste final a pagar es " + str(round(coste, 2)) + "€")

#*Ejercicios Condicionales*

#1.- age = int(input("¿Cuál es tu edad? "))
#if age < 18: 
    #print ("Eres menor de edad.")
#else:
  #  print("Eres mayor de edad.")

#2.- key = "contraseña"
#password = input("Introduce la contraseña: ")
#if key == password.lower():
   # print("La contaseña coincide")
#else:
  #  print("La contraseña no coincide")

#3.- n = int(input("Introduce un número entero: "))
#if n % 2 == 0:
   # print("El número " + str(n) + " es par")
#else:
    #print("El número " + str(n) + " es impar")

#4.- edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
#if edad < 4:
#   precio = 0
#elif edad <= 18:
#    precio = 4
#else:
#    precio = 10
# Mostrar precio
#print("El precio de la entrada es", precio, "€.")

#5.- Solucion 1
#name = input("¿Cómo te llamas? ")
#gender = input("¿Cuál es tu sexo (M o H)? ")
#if (gender == "M" and name.lower() < 'm') or (gender == "H" and name.lower() > 'n'):
#    group = "A"
#else:
#    group = "B"
#print("Tu grupo es " + group)

#Solucion 2
#name = input("¿Cómo te llamas? ")
#gender = input("¿Cuál es tu sexo (M o H)? ")
#if gender == "M":
#    if name.lower() < "m":
#        group = "A"
#    else:
#        group = "B"
#else:
#   if name.lower() > "n":
#       group = "A"
#    else:
#        group = "B"
#print("Tu grupo es " + group)

#*Ejercicios Bucles*

#1.-
#word = input("Introduce una palabra: ")
#for i in range(10):
#    print(word)

#2.-
#n = int(input("Introduce un número entero positivo: "))
#for i in range(1, n+1, 2):
#    print(i, end=", ")

#3.-
#for i in range(1, 11):
    #for j in range(1, 11):
     #   print(i*j, end="\t") 
    #print("")

#4.-
#key = "contraseña"
#password =""
#while password != key:
#    password = input("Introduce la contraseña: ")
#print("Contraseña correcta")

#5.-
#frase = input("Introduce una frase: ")
#letra = input("Introduce una letra")
#contador = 0
#for i in frase:
#    if i == letra:
#        contador += 1
#print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

