# # 1
from tkinter import colorchooser


i = 0
while (i < 15):
    i += 5
    print(i)


# # 2
while (i > -100):
    i -= 20
    print (i)  

# # 3
i = int(input('Ingresá un número'))
while (i != 0):
    i -= 1
    print('El valor del bucle es' , i)

# # 4
colores = ("naranja" , "azul", "verde" , "violeta", "rosa")
for color in colores:
    print('El color es: ' + color + '.')


# 5.- Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100. 
# Basta con que imprimas el valor de cada iteración.

for i in range(7, 800, 100):
    print (i - 7)

