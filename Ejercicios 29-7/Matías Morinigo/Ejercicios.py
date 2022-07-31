# # 1 Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5
i = 0
while True:
    i += 5
    if i == 20:
        break
    print(i)


# # 2 Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.
i = 0
while True:
    i -= 20
    if i == -120:
        break
    print(i) 


# 3 Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecución esta frase con el valor de 
# ejecución correspondiente: 'El valor del bucle es 10'...
i = 11
while True:
    i -= 1
    if i == -1:
        break
    print("El valor del bucle es:", i)


# 4 Crea un bucle for que itere la siguiente tupla y muestre una frase como esta en cada iteración: 'El color es: ' + color + '.'
color = {"rojo","verde","azul","naranja"}
for col in color:
    print("El color es:", col,".")


# 5 Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100. Basta con que imprimas el valor de cada iteración.
for i in range(7, 800, 100):
    print(i)
