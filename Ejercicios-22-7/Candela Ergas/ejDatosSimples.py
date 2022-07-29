from numbers import Real

#1.- Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print('Hola mundo!')


#2.- Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
saludo="Hola mundo!"
print(saludo)


#3.- Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde

horas=int(input("Cuantas horas trabajas?"))
paga=int(input("Cuánto te pagan por hora?"))

def sueldo(horas,paga):   
    total=horas*paga
    print("Si trabajas",horas,"hs cobrarás $",total)
sueldo(horas,paga)


#4.- Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales
pesoU= float(input("Cuanto pesas? (Ingresa el valor en kg por favor)"))
estatura= float(input("Cuanto medis?(Ingresa el valor en mts por favor)"))
imc= pesoU/ estatura**2
print("Tu índice de masa corporal es:",round(imc,2))

#5.- Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total
fresco=3.49
descuento= 60
panAyer= fresco-(fresco*descuento/100)
vendidas= int(input("Cuantas barras de pan que no son del día se vendieron?"))
print("El precio habitual es: ",fresco)
print("Se vendieron",vendidas," barras de pan y se hizo un descuento del ",descuento,"% porque no eran del día. El costo total fué ",round(panAyer*vendidas,2),"€")