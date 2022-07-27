# 5.- Una panadería vende barras de pan a 3.49€ cada una. 
# El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total

precio = 3.49
porcentajeDesc = 0.60
descuento = precio * porcentajeDesc
precioConDescuento = precio - descuento
precioConDescuento = round(precioConDescuento, 3) #Redondeo el número a 3 decimales
barrasConDescuento = int(input("Cantidad de barras vendidas que no son del día: "))
costoFinal = precioConDescuento * barrasConDescuento
costoFinal = round(costoFinal, 3) #Redondeo el número a 3 decimales
print("El precio habitual de la barra de pan es de: " + str(precio) + "€")
print("El descuento que se le hace a los panes que no están frescos es de " + str(descuento) + "€")
print("El precio del pan que no esta fresco es de: " + str(precioConDescuento) + "€")
print("El costo final total de las barras vendidas no frescas es de: " + str(costoFinal) + "€")
