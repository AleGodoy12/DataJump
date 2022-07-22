# 3.- Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
multiplicador = 0
limite = 10
numero = 10
while(multiplicador <= limite):
    producto = numero * multiplicador
    resultadoStr = str(numero) + " x " + str(multiplicador) + " = " + str(producto)
    multiplicador += 1
    print(resultadoStr)
