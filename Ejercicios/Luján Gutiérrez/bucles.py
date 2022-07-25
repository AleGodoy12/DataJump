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


#4  Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña = "queso"
i = 0
while(i<5):
    usuario = input('Contraseña')
    if(contraseña != usuario):
        input('Intentá nuevamente')
    i+=1
    print('No hay más intentos')

#5 Escribir un programa en el que se pregunte al usuario por una frase y una letra, y 
# muestre por pantalla el número de veces que aparece la letra en la frase
frase = input('Decime una frase')
letra = input('Decime una letra')







print("en la frase que ingresaste hay" , numLetras, letra, ".")

