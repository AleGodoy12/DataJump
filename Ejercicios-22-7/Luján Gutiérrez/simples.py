# SIMPLES

#1
print ('Hola Mundo')


#2
saludo = 'Hola Mundo'
print(saludo)


#3
nHorasTrabajadas = int(input('¿Cuántas horas trabajas por mes?'))
costoXhora = int(input('¿Cuál es el costo por hora'))
print (nHorasTrabajadas * costoXhora)


#4
peso = float(input('¿Cuál es tu peso?'))
estatura = float(input('¿Y tu estatura?'))
imc = (peso / estatura**2)
print ('Tu índice de masa corporal es', '{:.2f}'.format(imc))


#5
cantNoVendida = int(input('Cantidad de panes no vendidos ayer'))
barraPan = 3.49
descuento = abs((barraPan * 60) / 100)
print('Hay', cantNoVendida, 'panes a €' , descuento, 'cada una')



