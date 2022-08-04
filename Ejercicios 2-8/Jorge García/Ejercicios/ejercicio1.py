import math

# Escribir una función que reciba una muestra de números en una lista y 
# devuelva un diccionario con su media, varianza y desviación típica.

def calcularEstadisticas(datos):
    estadisticas = {}
    media = sum(datos)/len(datos)
    sumaDesvios = 0
    for i in datos:
        desvio = pow(i - media, 2)
        sumaDesvios += desvio
    varianza = sumaDesvios/len(datos)
    desvio = math.sqrt(varianza)
    estadisticas["Media"] = media
    estadisticas["Varianza"] = varianza
    estadisticas["Desvio"] = desvio
    return estadisticas

lista = [48, 48, 51, 52, 55, 56, 57, 58, 60, 61]
print(calcularEstadisticas(lista))