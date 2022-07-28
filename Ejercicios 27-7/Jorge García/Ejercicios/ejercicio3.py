# 3.- Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.

# tasaInteres = 2
# inversion = 50000
# tiempo = 2

inversion = float(input("Ingresa la cantidad que quieres invertir: "))
tasaInteres = float(input("Ingresa la tasa de interés anual [10 por ejemplo]: "))
tiempo = int(input("Ingresa los años que durará la inversión: "))

if(int(inversion) > 0 and int(tasaInteres) > 0 and int(tasaInteres) <= 100 and tiempo > 0):
    tasaInteres = tasaInteres / 100
    for anio in range(0, tiempo):
        ganancia = round(inversion * tasaInteres * 12, 2)
        capital = inversion + ganancia
        print(f"\nAño {anio+1} - Capital total obtenido: {capital}$ - Ganancia: {ganancia}$ - Inversión: {inversion}$")
        inversion = capital
else:
    print("Datos inválidos, intentalo más tarde.")