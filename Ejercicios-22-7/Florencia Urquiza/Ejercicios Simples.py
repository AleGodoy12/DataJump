#Ejercicios Tipo de datos simples:
#1-.Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print ("¡hola mundo!")


#2.- Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
saludo= "¡Hola Mundo!"
print (saludo)


#3.- Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
horasTrabajadas= int(input("Ingrese la cantidad de horas Trabajadas :"))
costoHora= int(input("Porfavor ingrese costo por hora :"))
print ("Le corresponde:", (horasTrabajadas*costoHora))


#4.- Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales
peso= float(input("Ingrese su peso en kg:"))
estatura= float(input ("Ingrese su estatura en m:"))
imc= round((peso/estatura),2)
print ("Tu indice de masa corporal es:", imc, "; donde ",imc, "es el índice de masa corporal calculado redondeado con dos decimales")


#5.- Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total
barra_pan= 3.49 ;
barra_vieja= 3.49*0.40 ;
barra_viejaDesc= 3.49*0.60
ventaDia= float(input ("Ingrese numero de barras de pan viejo vendidas: "))
print ("El precio habitual de una barra de pan es de: €", barra_pan, ". Por no ser fresca se le hace el descuento del 60% que seria de: €", barra_viejaDesc,
      ". El precio total por barra vieja será: €",barra_pan-barra_viejaDesc,". La venta de hoy fue : €",barra_vieja*ventaDia)

