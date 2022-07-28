# 2.- Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas

numero = int(input("Ingresa un número positivo: "))
texto = ""
if(numero > 0):
    for i in range(numero, -1, -1):
        if(i == 0):
            texto += f"{i}."
        else:
            texto += f"{i}, "
    print(texto)
else:
    print("Ojo! No es un número positivo.")