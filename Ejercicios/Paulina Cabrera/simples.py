#EJERCICIOS SIMPLES

#1.- Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print("¡Hola mundo!")

#2.- Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

mensaje = "¡Hola mundo!"
print(mensaje)

#3.- Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
#print("Ingrese la cantidad de horas que trabaja ")

hTrabajadas =int(input("Ingrese la cantidad de horas que trabaja por día: "))

pTrabajadas= int(input("Ingrese el valor que recibe por las horas que trabaja: "))

sueldoMensual = pTrabajadas * hTrabajadas
print("Lo que recibes por tus horas trabajadas es de: "+ str(sueldoMensual))



#4.- Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales


peso = float(input("Ingrese su peso actual: "))

estatura= float(input("Ingrese su altura actual: "))

imc = peso / (estatura **2)

print("Su índice de masa corporal es: ", str(imc)) 

#5.- Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total

cantidad= int(input("Ingrese la cantidad de pan no de dia vendido: "))

precioPan = 3.49
panNoDia = (3.49 * 60) / 100
print(f"El pan que no es del dia tiene un valor de: ", str(panNoDia) )

total = cantidad * precioPan

descuento = total * 60 / 100

print()
print("El total a pagar es de " + str(descuento)+ "€")
