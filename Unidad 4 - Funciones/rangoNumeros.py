numero=int(input('Ingrese un valor numerico:'))
if(numero>0 and numero<10): #Es posible unir condiciones con operadores logicos
    print('El numero se encuentra entre 0 y 10')
elif(numero>10 and numero<20):
    print('El numero se encuentra entre 10 y 20')
elif(numero>20 and numero<30):
    print('El numero se encuentra entre 20 y 30')
else:
    print('El numero no pertenece al rango')