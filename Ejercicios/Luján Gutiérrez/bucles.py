#BUCLES

#1
repeticion = input('Decime una palabra')
for i in range(0,10):
    print (repeticion)

#2
i = 0
array = []
while(i<10):
    num = int(input('Decime un número entero positivo'))
    if (num%2!=0):
        array.append(num)
    i +=1
print(array)

#3
num = int(input('Decime un número entero positivo'))
print ('Tabla de multiplicar del' , num)
for i in range(1,11):
    print(num , '*' , i , "=" , (num*i))


#4
contraseña = "queso"
i = 0
usuario = input('Contraseña')
while(i<5):
    if(contraseña != usuario):
        print('Intenta nuevamente')
        input('Contraseña')
    i+=1

#5
frase = input('Decime una frase')
letra = input('Decime una letra')

i=0
array = []
for L in frase:
    if (letra == L):
        array.append(L)
        letrasTotales = len(array)
    i+=1
print (letrasTotales)

