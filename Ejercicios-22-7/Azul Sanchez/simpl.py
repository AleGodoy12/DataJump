# Ejercicios simples:

# 1.- Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("hola")

# 2.- Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
Saludo= " ¡Hola " "Mundo! "
print(Saludo)

# 3.- Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
horasTrabajadas= float(input("Ingresa cuales son tus horas laborales: "))  #input: para pedirle al usuario que ingrese un dato
costePorHora= float(input("Igresa el coste de trabajo por hora: "))        #float:para definir el tipo de variable que va a ser(decimal)

pagaCorrespondiente= horasTrabajadas * costePorHora
print("Le corresponde: " + str(pagaCorrespondiente) + "pesos")

# 4.- Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales
peso= float(input("Ingrese su peso en kg: "))
altura= float(input("Infrese su altura en metros: "))

masaCorporal= peso/(altura * altura)
print("Tu índice de masa corpotal es:","{:.2f}".format(masaCorporal)) #:.2f indica la cantidad de decimales
                                                                      # .format es para indicar a que dato le queres agragar el 2f

# 5.- Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total

barrasDePan= int(input("Ingrese la cantidad de pan no fresco vendido: "))
precio= 3.49                                                                 
descuento= 0.6
coste= precio * barrasDePan * (1- descuento)
print("El descuento por no ser fresca es:" + str(descuento * 100) + "%")
print("El precio de una barra fresca es:" + str(precio) + "€")
print("El precio final es: " , "{:.2f}".format(coste))                     #:.2f: indicar la cantidad de decimales