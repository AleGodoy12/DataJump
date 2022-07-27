#Ejercicios de tipo simple

#1.- Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("¡Hola Mundo!")

#2.- Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
a = "¡Hola Mundo!"
print(a)

# 3.- Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por 
# pantalla la paga que le corresponde
horasTrabajadas = int(input("Ingrese las horas trabajadas: "))
costePorHora = int(input("Ingrese el coste por hora: "))
pago = horasTrabajadas * costePorHora

print(f"Su pago es de ${pago}")

# 4.- Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo 
# almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal 
# calculado redondeado con dos decimales
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
indice = peso / (altura * altura)

print(f"SU indice de masa corporal es {indice:.2f}")

# 5.- Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un 
# programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio 
# habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total
PRECIO_PAN = 3.49
DESCUENTO_PAN = 0.60

cantidadVendidas = int(input("Ingrese la cantidad de pan vendido: "))

costeSinDesc = PRECIO_PAN * cantidadVendidas
costeConDesc = (costeSinDesc) * DESCUENTO_PAN
costeTotal = (costeSinDesc) - costeConDesc

print(f"Precio de la barra de pan {PRECIO_PAN}€")
print(f"Descuento sobre precio {DESCUENTO_PAN * 100}%")
print(f"El coste total es de ${costeTotal:.2f}")
