# CONDICIONALES

#1
edad = int(input('Decime tu edad'))
if (edad <= 18):
    print ('Sos menor de edad')
else: 
    print ('Sos mayor de edad')


#2
contraseña = input('Contraseña por favor')
if (contraseña == "CHEESE" or contraseña == "cheese"):
    print (True)
else:
    print(False)


#3 
num = int(input('Decime un número'))
if (num%2!=0):
    print ('Es impar')
else:
    print('Es par')


#4
edad = int(input('Decime tu edad'))
if (edad < 4):
    print ('La entrada es gratis')
elif (edad == 4 or edad <= 18):
    print('La entrada sale 5€')
else:
    print('La entrada sale 10€')


#5
mujeres = ("A","B","C","D","E","F","G","H","I","J","K","L","M")
hombres = ("N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")
nombre = input('Decime tu nombre')
genero = input('Decime tu género - F/M/OTRO')

if ((nombre.startswith(mujeres) and genero == "F") or (nombre.startswith(hombres) and genero == "M")):
    print ('Sos del grupo A')
else:
    print('Sos del grupo B')
