# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

numerosGanadores = []
for i in range(5):
    numero = int(input("Ingresa un número ganador: "))
    numerosGanadores.append(numero)
numerosGanadores.sort()
print(numerosGanadores)