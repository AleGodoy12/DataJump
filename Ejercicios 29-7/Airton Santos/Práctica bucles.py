# 1.- Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5

def incrementoCinco():
    
    x = 0 
    acumulador = 0

    while x < 15:
        acumulador += 5
        x += 5 
        print(acumulador)

incrementoCinco()


# 2.- Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.

def decrementoVeinte():
    x = 0
    acumulador = 0 

    while x > -100:
        acumulador -= 20
        x -= 20
        print(acumulador)

decrementoVeinte()

# 3.- Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecución esta frase con el 
# valor de ejecución correspondiente: 'El valor del bucle es 10'...

def decremento(i):

    while i > 0:
        i -= 1 
        print(f"El valor del bucle es {i}")

decremento(10)

#4.- Crea un bucle for que itere la siguiente tupla y muestre una frase como esta en cada iteración: 'El color es: ' + color + '.'

def colores (tupla):
    i = 0

    for color in tupla:
        print(f"El color es: {color}.")
        i += 1 

colores(("Amarillo", "Verde", "Violeta"))

# 5.- Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100.
#  Basta con que imprimas el valor de cada iteración.

def iteracion():

    for i in range(7, 700, 100):
        print(i)

iteracion()


#Ejercicio opcional 

x = 0 

while x <= 30:
    print(f"El valor del bucle es:  {x}.")
    x += 1 

    if x == 15:
        print(f"Se rompió la ejecución del bucle cuando x valía {x}")
        break

    if x == 4 or x == 6 or x == 10:
        print(f"Se saltó el valor {x} de x")
        continue


