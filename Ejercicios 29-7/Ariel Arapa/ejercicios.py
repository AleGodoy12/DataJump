# 1.- Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5
# x = 0
# while True:
#     x += 5
#     print(x)
#     if x == 15:
#         break



# 2.- Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.
# y = 0
# while True:
#     y -= 20
#     print(y)
#     if y == -100:
#         break



# 3.- Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecución esta frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'...
# a = 10
# while a > -1:
#     print(f"El valor del bucle es {a}")
#     a -= 1



# 4.- Crea un bucle for que itere la siguiente tupla y muestre una frase como esta en cada iteración: 'El color es: ' + color + '.'
# tupla = ("rojo", "amarillo", "naranja")

# for i in tupla:
#     print(f"El olor es: {i}.")




# 5.- Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100. Basta con que imprimas el valor de cada iteración.
# for i in range(7, 700, 100):
#     print(i)


# -Opcional-
# **Crea un bucle while con las siguientes características:
# El valor inicial de la variable x será de 0.
# El valor de incremento será 1.
# La condición de salida del bucle será mayor o igual a 30.
# La ejecución se deberá romper cuando x valga 15.
# Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
# Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
# En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
# Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 'Se rompió la ejecución del bucle cuando x valía ' + x **
x = 0

while x <= 30:
    print(f"El valor del bucle es: {x}")
    x+=1
    if(x == 4 or x == 6 or x == 10):
        print(f"Se salto el valor {x} de x")
        continue
    if(x==15):
        print(f"Se rompio la ejecucion cuando el bucle valia: {x}")
        break


