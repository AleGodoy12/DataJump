# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

numerosGanadores = []
intentos = 6

while intentos > 0:
    numero = int(input("Ingresa un número ganador entre 1 y 49: "))
    if(numero in numerosGanadores):
        print(f"El número {numero} ya estaba, ingresa otro.")
        continue
    if(numero > 0 and numero < 50):
        numerosGanadores.append(numero)
        intentos -= 1
    else:
        print("Número inválido, debes ingresar un número entre 1 y 49")
        
numerosGanadores.sort()
print(f'Números ganadores: {numerosGanadores}')