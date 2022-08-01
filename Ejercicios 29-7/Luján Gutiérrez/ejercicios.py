# # 1
# from tkinter import colorchooser


# i = 0
# while (i < 15):
#     i += 5
#     print(i)


# # 2
# while (i > -100):
#     i -= 20
#     print (i)  

# # 3
# i = int(input('Ingresá un número'))
# while (i != 0):
#     i -= 1
#     print('El valor del bucle es' , i)

# # 4
# colores = ("naranja" , "azul", "verde" , "violeta", "rosa")
# for color in colores:
#     print('El color es: ' + color + '.')


# 5.- Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100. 
# Basta con que imprimas el valor de cada iteración.

for i in range(7, 800, 100):
    print (i - 7)

# -Opcional-

# **Crea un bucle while con las siguientes características:
# El valor inicial de la variable x será de 0.                
# El valor de incremento será 1.                               
# La condición de salida del bucle será mayor o igual a 30.    
# La ejecución se deberá romper cuando x valga 15.   break x = 15 
# Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
# Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
# En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
# Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 'Se rompió la ejecución del bucle cuando x valía ' + x **