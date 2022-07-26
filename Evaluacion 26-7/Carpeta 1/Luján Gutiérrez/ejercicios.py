#1
edad = int(input('Ingresá tu edad'))

if (edad < 4):
    print('Ingresas gratis')
elif (edad <= 18):
    print('Pagas 5€')
else:
    print('Pagas 10€')

#2
frase = input('Ingresá una frase')
letra = input('Ingresá una letra')
i = 0
array = []

for L in frase:
    if (L == letra):
       array.append(L)
       letrasTotales = len(array)
    i += 1
print(letrasTotales) 

#8/10 letrasTotales no se muestra definido. Lo vemos.
    