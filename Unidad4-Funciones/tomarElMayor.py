i=3 # Repite el proceso 3 veces
while(i>0):
    numero=int(input('Ingrese un valor numerico:'))
    if(numero>0 and numero<10):
        print('El numero se encuentra entre 0 y 10')
    elif(numero>10 and numero<20):
        print('El numero se encuentra entre 10 y 20')
    elif(numero>20 and numero<30):
        print('El numero se encuentra entre 20 y 30')
    else:
        print('El numero no pertenece al rango')
    i=i-1