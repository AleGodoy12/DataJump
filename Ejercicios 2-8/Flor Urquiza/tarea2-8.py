#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre
# por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for i in asignaturas :
    print ("Yo estudio, ", i)


#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

lista= []
ganadoresLoteria= input("Ingrese los numeros ganadores de la loteria primitiva: ")
for i in ganadoresLoteria:
    lista= sorted(ganadoresLoteria)

print(lista)

#6.- Escribir un programa que almacene en una lista los siguientes precios, 
# 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

