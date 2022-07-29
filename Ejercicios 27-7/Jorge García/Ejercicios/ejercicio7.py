# 7.- Escribir una función que calcule el área de un círculo y otra que calcule
#  el volumen de un cilindro usando la primera función

import math

def calcularAreaCirculo(radio):
    area = math.pi * radio**2
    return round(area, 3)

def calcularVolumenCilindro(radio, altura):
    area = calcularAreaCirculo(radio)
    volumen = area * altura
    return volumen

radio = 9
areaCirculo = calcularAreaCirculo(radio)
altura = 14
volumenCilindro = calcularVolumenCilindro(radio, altura)
print(f"El área del circulo es: {areaCirculo}")
print(f"El volumen del cilindro es: {volumenCilindro}")
