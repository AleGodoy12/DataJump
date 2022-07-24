# 1.- Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

""" print ("Hola mundo") """

# 2.- Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

""" programa = "Hola mundo"

print (programa ) """

# 3.- Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
 
""" horasTrabajadas = int (input ("Escribir las horas trabajadas: "))
print ("horas trabajadas = ", horasTrabajadas)

numeroHoras =int (input ("El coste por hora es: "))
print ("Coste por hora es= ", numeroHoras)

paga = horasTrabajadas * numeroHoras
print ("La paga correspondiente es: ", paga) """


# 4.- Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales

""" peso = float (input("Escriba su peso : "))
estatura = float (input("Escriba su estatura: "))

calculoMasa = peso / (estatura * estatura)

print ("El IMC es: ", calculoMasa) """


# 5.- Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total

""" cantidadPanVendidas = float (input("El número de pan de barras vendidas de pan que no son del día: "))
precio = 3.49 
descuento = 0.60

print ("El pan tiene un precio de: ", precio, "€")
print ("Se le hace un descuento de: 60 %")

precioFinal = cantidadPanVendidas * precio * descuento
print ("Precio final es: ", precioFinal, "€" ) """


