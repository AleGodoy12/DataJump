###Ejercicios Tipo de datos simples:

#1.- Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print ("Hola mundo")
#2.-  Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
a= "Hola mundo"
print (a)
#3.- Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
horasTrab=float(input("Ingrese la cantidad de horas trabajadas "))
precioPorHora=float(input("Ingrese cuanto cobra por hora "))
pago= horasTrab*precioPorHora 
print("Su paga es: $", pago)
#4.- Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales
altura=float(input("Ingrese su altura (en metros) "))
peso=float(input("Ingrese su peso (en kilogramos) "))
indice= peso/(altura**2) 
aprox= round(indice, 2)
print("Su IDMC es: ", aprox)

#5.- Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total
barrasDePan = 3.49
cant=int(input("Ingrese la cantidad de pan vendido NO frescas "))
precio = cant*barrasDePan
precioConDesc= precio*60/100
aprox= round(precioConDesc, 2)
print("Barras de pan por ", cant )
print("Precio de barra de pan = ", barrasDePan,"€")
print("Descuento sobre el precio")
print("Precio total= ", aprox, "€")
